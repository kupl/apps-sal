def check(password,n,a):
	for i in range(n):
		if (password[0] == a[i][1]):
			for j in range(n):
				if (password[1] == a[j][0]):
					return True

	if (password in a):
		return True

	return False

password = input()
n = int(input())
a = []
for i in range(n):
	a.append(input())

if (check(password,n,a)):
	print('YES')
else:
	print('NO')



