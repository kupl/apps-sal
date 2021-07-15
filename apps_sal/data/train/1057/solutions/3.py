def checkmagic(n):
	for i in range(0, len(n)):
		if n[i] != '4' and n[i] != '7':
			return False
	return True

def nextmag(n):
	n = str(n)
	n = list(n)
	n = n[::-1]
	n[0] = str(int(n[0])+1)
	s = []
	for i in range(0, len(n)):
		s.append('7')
	if int(''.join(n[::-1])) > int(''.join(s)):
		n.append('0')
	
	i=0
	while (checkmagic(n) == False) and (i < len(n)):
		if int(n[i]) < 4:
			n[i] = '4'
		elif int(n[i]) < 7:
			n[i] = '7'
		else:
			n[i] = '4'
			n[i+1] = str(int(n[i+1])+1)
		i += 1
	
	return (''.join(n[::-1]))

T = int(input())
a = []

for i in range(0, T):
	k = int(input())
	a.append(nextmag(k))

for e in a:
	print(e)
