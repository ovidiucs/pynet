#!/usr/bin/env python2
'''
1. Use the split method to divide the following IPv6 address into groups of 4
hex digits (i.e. split on the ":")

FE80:0000:0000:0000:0101:A3EF:EE1E:1719
'''

ipv6_address = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'
ipv6_address_section = ipv6_address.split(":")

print '\n' +'IPv6 sections below'+ '\n'
print ipv6_address_section  

print "joined" +'\n\n'+  ":".join(ipv6_address_section)

