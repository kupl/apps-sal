password = input()
n = int(input())
a = []
for i in range(n):
	a.append(input())
b = []
for w in a:
	for w2 in a:
		b.append((w+w2)[:2])
		b.append((w+w2)[1:3])
		b.append((w+w2)[2:])

if password in b:
	print("YES")
else:
	print("NO")
