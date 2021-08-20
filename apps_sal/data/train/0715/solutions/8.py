import string
s = [x for x in str(input())]
d = {}
p = 0
for i in range(26):
    d[i + 1] = string.ascii_uppercase[i]
k = list(d.keys())
v = list(d.values())
for i in s:
    if i in v:
        p += 28 - k[v.index(i)]
    else:
        pass
print(p)
