import itertools

file_characters = open("pc_02.txt", "rt")
characters = file_characters.read()
file_characters.close()

secret_word = ""
for l in characters:
	count = str.count(characters, l)
	if count == 1:
		secret_word += l

print(secret_word)