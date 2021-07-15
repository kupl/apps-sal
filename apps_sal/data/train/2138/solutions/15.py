a = input()
b = input()

sa = 0
for s in a:
	if s == '1':
		sa += 1

sb = 0
for s in b:
	if s == '1':
		sb += 1

if sa >= sb:
	print("YES")
else:
	if sb%2 == 0:
		if sa == sb-1:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
