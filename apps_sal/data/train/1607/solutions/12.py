s = input()
r = ''
for i in s:
	if i in 'QA':
		r += i
while len(r) and r[0] != 'Q':
	r = r[1:]
while len(r) and r[-1] != 'Q':
	r = r[:-1]
res = 0
for i in range(len(r)):
	if r[i] == 'A':
		res += r[:i].count('Q') * r[i + 1:].count('Q')
print(res)
