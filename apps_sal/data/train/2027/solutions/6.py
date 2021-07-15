from sys import stdin, stdout
s = input().strip()
n = len(s)
left = 0
right = n-1
vs = [0]*n
for i in range(n):
	if(s[i] == 'l'):
		vs[right] = str(i+1)
		right -= 1
	else:
		vs[left] = str(i+1)
		left += 1
print('\n'.join(vs))

