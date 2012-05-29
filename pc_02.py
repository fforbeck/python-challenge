file_characters = open("pc_02.txt", "rt")
characters = file_characters.read()
file_characters.close()

import re
matcher = re.compile('[a-z|A-Z|0-9]')
#considerar menor ocorrencia dos chars
print(matcher.match(characters))
