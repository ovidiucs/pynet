print "Input address"
octets = raw_input('> ')
s = octets.split('.')

if len(s) == 3:
    s.append('0')
elif len(s) == 4:
    s[3] = '0'

print "NETWORK NUMBER \t FIRST_OCTET_BINARY \t FIRST_OCTET_HEX"
print "%0s %15s %15s" % ('.'.join(s), bin(int((s[0]))), hex(int((s[0]))))
