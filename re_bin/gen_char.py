#generates ASCII values to overwrite 32-bit memory addresses
import sys
from functools import reduce

output = ""

	 
if len(sys.argv) < 2:
	for i in range(65,91):
		output += chr(i)*4 #since ASCII char are 8 bits (2^8 possible chars) need 4 of them to fill 32 bit register

else:
	replace_pos = ord(sys.argv[1])
	replace_word = sys.argv[2]
	
	#parse hex characters to give correct output
	#if "\x" in replace_word:
	#	replace_word = reduce((lambda x, y: x + y), replace_word.split("\x"))	
 	#	print replace_word

	for i in range(65,91): 
		if i == replace_pos:
			output += replace_word #assumes that replace_word is exactly 32 bitsor else we would have memory alignment issues
		else:
			output += chr(i)*4

print output
	
			
			
