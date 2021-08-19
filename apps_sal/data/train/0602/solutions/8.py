l = list(map(str, input().split()))
ma = float('inf')
for i in l:
    if len(i) < ma:
        ma = len(i)
        v = i
n = len(l)
k = []
for i in range(n):
    k.append(l[i])
    if i != n - 1:
        k.append(v)
k.append(v)
k.insert(0, v)
st = ' '.join(k)
print(st)
