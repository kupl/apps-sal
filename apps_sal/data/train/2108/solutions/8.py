a, b = input().split()
n = int(input())

couples = []

for i in range(n):
	couples.append(input().split())

for j in range(n):
	print(a, b)
	if couples[j][0] == a:
		a = couples[j][1]
	else:
		b = couples[j][1]

print(a, b)
