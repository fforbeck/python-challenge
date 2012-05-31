import re
import itertools

especial_letters = set()

in_file = open('pc_03.txt', "rt")
while True:
	line = in_file.readline()
	if not line:
		break
	
	match = re.search('[A-Z]{3}[a-z]{1}[A-Z]{3}', line)
	if match is not None:
		especial_letters.add(match.group()[3])
	    
in_file.close()

print(''.join(sorted(especial_letters)))