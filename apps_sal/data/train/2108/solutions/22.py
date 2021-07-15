a, b = input().split()
N = int(input())
print(a, b)
for n in range(N):
	c, d = input().split()
	if c == a:
		a = d
	elif c == b:
		b = d
	elif d == a:
		a = c
	elif d == b:
		b = c
	print(a, b)
