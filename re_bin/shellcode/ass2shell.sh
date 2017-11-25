#!/bin/bash

OPCODE=`awk -F $'\t' '/^\s/ { print $2}'`
HEX=""
for code in $OPCODE; do
	HEX="$HEX\x$code"
done
echo $HEX
