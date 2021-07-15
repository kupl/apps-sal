import sys
N = 1<<20
ar = [0]*N
n = int(input())
for i in range(0, n):
    inp = input().split()
    ar[int(inp[0])+1]= int(inp[1])
for i in range(N):
    ar[i] = (1 if ar[i]>=i else ar[i-ar[i]-1]+1) if ar[i] else ar[i-1]
print(n-max(ar))

