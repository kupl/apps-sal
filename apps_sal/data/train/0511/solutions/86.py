import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

total = 0

for i in range(n):
	if i == 0:
		total = a[i]
	else:
		total = total ^ a[i]
		
b = []
for i in range(n):
	b.append(str(a[i] ^ total))

print(' '.join(b))
