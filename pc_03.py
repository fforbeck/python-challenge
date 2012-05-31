import re

_file = open("pc_03.txt", "rt")
data = _file.read()
_file.close()

print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))