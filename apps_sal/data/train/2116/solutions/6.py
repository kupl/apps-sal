m = int(input()) - 1
k = input()
r = ''
i = 97
t = [k]
while 1:
    q = chr(i)
    p = []
    for d in t:
        for s in d.split(q):
            if len(s) > m: p += [s]
    if not p: break
    r += q * k.count(q)
    i += 1
    t = p
y = chr(i)
for d in t:
    i = 0
    for x in d:
        if x == y: j = i
        if i == m:
            r += y
            i -= j
            j = 0
        else: i += 1
print(r)
