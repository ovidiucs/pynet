import std.stdio;
import std.algorithm;
import std.array;

void main()
{
   auto ipv6_address = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719";
   auto ipv6_split = split(ipv6_address,':');
   writeln(ipv6_split);
   
   writeln("Joined");
   writeln(join(ipv6_split,':'));
}

