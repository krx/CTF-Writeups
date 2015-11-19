# CSAW Finals 2015: randsomewhere - Forensics 300

For this challenge, we are given an image file called `randsomewhere.img`

Running `file` reveals that this is a DOS boot sector

```bash
$ file randsomewhere.img 
randsomewhere.img: DOS/MBR boot sector
```

To look at the files inside, I opened the image with testdisk:

![alt text](https://raw.githubusercontent.com/kareemroks101/CTF-Writeups/master/CSAW%2015%20Finals/for300%20-%20randsomewhere/testdisk.png "Testdisk Output")

There are two files of interest here: `flag.png.encrypted` and `rand_somewhere.rb` (which was deleted)

## File Analysis

Looking at `flag.png.encrypted`, it contains data that doesn't resemble PNG data, and this header:

```
Encrypted by randsomewhere. Send 1 BTC to bitcoin address Rm9yIHRoaW5ncyB0byByZXZlYWwgdGhlbXNlbHZlcyB0byB1cywgd2UgbmVlZCB0byBiZSByZWFkeSB0byBhYmFuZG9uIG91ciB2aWV3cyBhYm91dCB0aGVtLg==Visit Tor hidden service http://fakehiddenservicenotpartofthechallenge.onion/?id=006AFF07 to confirm your payment and receive the decryption program.
```

The header contains some base64 data and a dead onion link, both of which lead to nothing useful

Here are the contents of `rand_somewhere.rb`:

```ruby
require 'openssl'

class RandSomewhere

  def initialize(bitcoin_addr, hidden_service_name, id_num)
  	rand = Random.new(seed = Time.now.to_i)
    key_length = 42
    @key = rand.bytes(key_length)
    @algo = "AES-256-CBC"
    @header =  "Encrypted by randsomewhere. Send 1 BTC to bitcoin address #{bitcoin_addr}"
    @header << "Visit Tor hidden service http://#{hidden_service_name}.onion/?id=#{id_num} to confirm your payment and receive the decryption program."
  end

  def encrypt_file(filename)
    cipher = OpenSSL::Cipher.new(@algo)
    cipher.encrypt
    cipher.key = @key
    data = IO.binread(filename)  
    encrypted_data = cipher.update(data)
    encrypted_data << cipher.final
    IO.binwrite(filename + ".encrypted", @header + encrypted_data)
  end

  def decrypt_file(filename)
    cipher = OpenSSL::Cipher.new(@algo)
    cipher.decrypt
    cipher.key = @key
    data = IO.binread(filename)
    file_data = data[@header.length..-1] # Skip the header.
    plaintext = cipher.update(file_data)
    plaintext << cipher.final
    plaintext_filename = filename + ".decrypted"
    IO.binwrite(plaintext_filename, plaintext)
  end

end
```

Right away we can see a few things:
- The file is encrypted with AES-256-CBC, and the header is added at the beginning
- A random key is generated using `Time.now`
- To decrypt the file, the header is skipped, and the remaining data is decrypted with the same key

## Decryption

What's interesting about this program is how the key is generated. In the first line of `initialize(...)`, `Time.now` is used as the **seed** for the random number generator. Then, assuming `encrypt_file(...)` is called immediately, it creates a new file with the encrypted data. This means that the creation time of the file should exactly match the time used as the seed for the key. But when was the file created? Back to testdisk:

```
 -rwxr-xr-x     0     0      4731 13-Nov-2015 01:08 flag.png.encrypted
```

**NOTE:** To make things easier, I made a copy of `flag.png.encrypted` with the header removed called `noheader.encrypted`

Now with the file creation time known, I wrote a script to decrypt the file with the testdisk time as the seed:

```ruby
require 'openssl'
t = Time.new(2015,11,13,1,8, 0)
rand = Random.new(seed = t.to_i)
cipher = OpenSSL::Cipher.new('AES-256-CBC')
cipher.decrypt
cipher.key = rand.bytes(42)
cipher.padding = 0
data = IO.binread('noheader.encrypted')
plaintext = cipher.update(data)
plaintext << cipher.final
IO.binwrite('flag.png', plaintext)
```

Now running the script:

```bash
$ ruby dec.rb 
$ xxd flag.png
0000000: 69a1 3a9f 3893 8e09 fe86 95ff eeaa 60a5  i.:.8.........`.
0000010: c45a 0067 8e89 584c 0acf f861 4b90 0665  .Z.g..XL...aK..e
...
0001110: e990 e2ba 6541 1ff0 e427 db7e 573b b208  ....eA...'.~W;..
0001120: 5ecb 9be9 b352 92fe 9640 f26f e0db 640d  ^....R...@.o..d.
```

But now we have another problem, this still doesn't look like PNG data. My first assumption was that the key had to be wrong. One of my teammates suggested to sweep around the time found in testdisk and use each time as a seed, since the file may not have been created immediately after the key was generated. Going along with this, I modified the earlier script to try using every time in a range before and after the testdisk time, and to only save files that had distinctive PNG data, like the strings `PNG` and `IEND`. I ended up sweeping a full 24hr before and after the time found in test disk before it worked.

Here is the modified script:

```ruby
require 'openssl'
off = 3600*24
t = Time.new(2015,11,13,1,8, 0)
t -= off # 24hr before
for i in 0..off*2 # to 24hr after
	t += 1
	rand = Random.new(seed = t.to_i)
	cipher = OpenSSL::Cipher.new('AES-256-CBC')
	cipher.decrypt
	cipher.key = rand.bytes(42)
	cipher.padding = 0
	data = IO.binread('noheader.encrypted')
	plaintext = cipher.update(data)
	plaintext << cipher.final
	if plaintext.include? 'PNG' and plaintext.include? 'IEND'
		puts "FOUND PNG AT #{i}"
		IO.binwrite('flag.png', plaintext)
		break
	end
end
```

And running it:

```bash
$ ruby dec.rb 
FOUND PNG AT 50457
```

Great! It found a PNG, let's open it up:

![alt text](https://raw.githubusercontent.com/kareemroks101/CTF-Writeups/master/CSAW%2015%20Finals/for300%20-%20randsomewhere/flag.png "flag.png")

And now we have the flag:

```
yo mama so fat, she can't store files larger than 4 GB
```
