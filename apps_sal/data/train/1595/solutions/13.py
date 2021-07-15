def ct(string):
	i = 0
	num = 0
	while( i < 10):
		num *= 2
		if(string[i] == 'w'):
			num += 1
		i += 1
	return num
	
def convert(string):
	i = 0
	num = 0
	while( i < 10):
		num *= 2
		if(string[i] == '+'):
			num += 1
		i += 1
	return num

t = int(input())
while(t > 0):
	pic = input()
	m = ct(pic)
	tab = {m : 1}
	n = int(input())
	
	while(n > 0):
		filtr = input()
		num = convert(filtr)
		k = list(tab.keys())
		newtab = tab.copy()
		
		for i in k:
			value = tab[i]
			new = num ^ i
			z = tab.get(new,0)
			if(z > 10000000 or value > 10000000):
				newtab[new] = (z + value) % 1000000007
			else:
				newtab[new] = (z + value)
		n -= 1
		tab = newtab.copy()
	print(str(tab.get(0,0)))		
	t -= 1
	
