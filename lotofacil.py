Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def lotofacil():
	jogo = []
	while len(jogo) < 15:
		num = random.randint(1,25)
		if num in jogo:
			continue
		else:
			jogo.append(num)
			print(sorted(jogo))


			
