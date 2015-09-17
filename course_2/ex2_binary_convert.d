import std.stdio;
import std.string;
import std.conv;
import std.format;

void main()
{
   write(" > ");
   string ip_address = chomp(readln);
   string[] arr = split(ip_address,'.');
   writefln("%20s %20s %20s %20s", "first octet", "second octet", "third octet",
         "fourth octet");
   foreach(i; arr[]){
      writef("%20.08b",to!int(i)); 
   }write('\n');
}
