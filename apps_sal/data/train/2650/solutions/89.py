n,l = map(int,input().split())
ans = ''
k = []
for i in range(n):
    s = input()
    k.append(s)
k.sort()
for i in k:
    ans +=i
print(ans)
