
print "Input the network"
octets = raw_input('> ')
s      = octets.split('.')

first_octet   = int(s[0])
second_octet  = int(s[1])
third_octet   = int(s[2])
fourth_octet  = int(s[3])

print "%0s %20s %20s %20s" % \
              ("first_octet", "second_octet", "third_octet", "fourth_octet")
              print "%0s %20s %20s %20s" % \
              ('{0:08b}'.format(first_octet),'{0:08b}'.format(second_octet),
               '{0:08b}'.format(third_octet),'{0:08b}'.format(fourth_octet))
