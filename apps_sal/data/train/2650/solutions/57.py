(n, l) = list(map(int, input().split()))
s = []
for i in range(n):
    s.append(input())
s.sort()
res = ''
for i in range(n):
    res += s[i]
print(res)
