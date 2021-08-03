n = int(input())
k = 0
d = {}
for _ in range(n):
    a = list(map(int, input().split()))
    a.sort()
    a = str(a)
    if a in d.keys():
        d[a] = d[a] + 1
    else:
        d[a] = 1
for key in d:
    if(d[key] == 1):
        k = k + 1
print(k)
