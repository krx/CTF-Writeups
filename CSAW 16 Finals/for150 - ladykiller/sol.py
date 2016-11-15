#!/usr/bin/env python2
from subprocess import check_output
import re
import glob
from string import printable
from itertools import groupby

# Make sure these files are sorted numerically
# i.e. "date.3" needs to be before "date.11"
cores = sorted(glob.glob('date.*'), key=lambda s: int(s.split('.')[1]))

# Dump the registers of every core file with gdb
gdb_cmd = ['gdb', '-batch']
for core in cores:
    gdb_cmd += [
        '-ex', 'core-file {}'.format(core),
        '-ex', 'info registers'
    ]
regs = check_output(gdb_cmd)

# Pull out all values of rdx as chars
rdxs = [chr(int(match.group(1), 16) & 0xff) for match in re.finditer(r'rdx\s+0x([a-fA-F0-9]+)', regs)]

# Get rid of duplicate and unprintable chars
print ''.join([val for val, grp in groupby(rdxs) if val in printable])

