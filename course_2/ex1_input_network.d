import std.stdio;
import std.string;
import std.conv;
import std.format;

void main()
{
   write(" > " );
   string ip_address = chomp(readln);
   int firstOctet = to!int(split(ip_address,'.')[0]);
   writeln("NETWORK NUMBER FIRST_OCTET_BINARY FIRST_OCTET_HEX");
   writefln("|%s| |%-17.08b| |%-17x|", ip_address, firstOctet, firstOctet);
}
