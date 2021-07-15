s = input()
l = [0] * len(s)
a = 0
b = len(s) - 1
for i in range(len(s)):
	if s[i] == 'l':
		l[b] = str(i + 1)
		b -= 1
	else:
		l[a] = str(i + 1)
		a += 1
print('\n'.join(l))
