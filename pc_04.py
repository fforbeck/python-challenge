import urllib2, re, sys

uri = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'

def get_next(nothing):
	request = request = urllib2.Request(uri + nothing)
	result = str(urllib2.urlopen(request).read())
	if 'html' in result:
		print("secret word :D -----> " + result)
		sys.exit()

	next_nothing = ''.join(re.findall('\d', ''.join(re.findall('nothing is \d+', result))))
	if (next_nothing == ''):
		next_nothing = str(int(nothing) / 2)

	return next_nothing

i = 0
while (i <= 270):
	nothing = get_next(nothing)
	print(nothing) 
	i = i + 1