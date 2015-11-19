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
