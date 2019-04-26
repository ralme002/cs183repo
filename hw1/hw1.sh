#!/bin/bash

#catch all variables coming in first

for FILE1 in "$@"
do
	while IFS= read line
	do
	echo "$line"
	done<"$FILE1"
done

