import std.stdio;
import std.array;
import std.string;

void main()
{
   char[] ip_address;
   readln(ip_address);
   ip_address = chomp(ip_address);
   writeln(split(ip_address,'.'));
}
