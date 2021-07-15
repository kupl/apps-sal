n = int(input())
s = [0] * 7
for _ in range(n):
	mes = input()
	for i in range(7):
		s[i] += (mes[i] == '1')
print(max(s))
