s = input()
sec = []
fir = []
n = int(input())
for i in range(n):
	s1 = input()
	sec.append(s1[1])
	fir.append(s1[0])
	if s1 == s:
		print('YES')
		break
else:
	if s[0] in sec and s[1] in fir:
		print('YES')
	else:
		print('NO')
