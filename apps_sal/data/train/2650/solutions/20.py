nl = input().split()

N = int(nl[0])
L = int(nl[1])

lst = []

for i in range(N):
   lst.append(input())

lst.sort()

ans = ''

for s in lst:
   ans += s

print(ans)
