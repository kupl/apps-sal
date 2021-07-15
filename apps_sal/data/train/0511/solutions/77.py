import sys

# E - Red Scarf
N = int(input())
a = list(map(int, input().split()))

xor = a[0]

for i in range(1, N):
  xor ^= a[i]

ans = []

for i in range(N):
  ans.append(xor ^ a[i])

print(' '.join(map(str, ans)))
