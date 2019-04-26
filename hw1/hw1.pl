#!/bin/perl
foreach my $a(@ARGV)
{
	my $file = $a;
	open(FH, '<', $file) or die $!;
	while(<FH>)
	{
	print $_;
	}
	print "\n";
	#print "$a\n"
}
