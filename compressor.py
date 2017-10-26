import re
import sys

out = ''	

with open('./bind_listener.py') as fd:
	for line in fd.readlines():
		m = re.search('[a-zA-Z]', line)
	 	if m:
			out += line.replace('\n',';')
print out			  	
