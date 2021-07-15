s = input()
zero = -1

for i in range(len(s)):
	if s[i] == '0':
		zero = i
		break

if zero == -1:
	print(s[1:])
else:
	print(s[:zero] + s[zero+1:])
