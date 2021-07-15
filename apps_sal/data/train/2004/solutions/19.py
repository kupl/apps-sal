b = input().strip()

p = b.find('0')

os = ''
if p != -1:
	os = b[:p] + b[p+1:]
else:
	os = b[1:]

print(os)
