import re

c = 0
ds = [{},{}]
coords = {}
dup = 0
n = int(input())
for i in range(0, n):
    t = re.split(' ', input())
    T = tuple(t)
    coords[T] = 1 + (0 if (T not in coords) else (coords[T]))
    dup += coords[T]-1
    for j in range(0, len(ds)):
        ds[j][t[j]] = 1 + (0 if (t[j] not in ds[j]) else (ds[j][t[j]]) )

for i in range(0, len(ds)):
    for k, v in list(ds[i].items()):
        c += v*(v-1)/2

print(int(c-dup))
    

