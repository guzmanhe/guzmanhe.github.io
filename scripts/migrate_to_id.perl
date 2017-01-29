#!/usr/bin/perl

while(<STDIN>)
{
    if (m/^(.*)img\: ?(.*)$/)
    {
        print "$1id: $2\n";
        
    }
    print;
}