#!/usr/bin/env python2

'''
Here is an example using this script where I echo an IP address into it and then
the IP address is split into its octets.

$ echo '192.168.1.1'  | ./test3.py 
['192', '168', '1', '1\n']
'''

import fileinput

for line in fileinput.input():
        print line.rstrip().split('.')
