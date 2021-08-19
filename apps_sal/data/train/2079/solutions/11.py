import math
q = int(input())
s = {}
o = []
for i in range(q):
    r = list(map(int, input().split()))
    (a, b) = (r[1], r[2])
    if r[0] == 2:
        o.append(0)
    while a != b:
        if math.log2(a) > math.log2(b) and a != 1:
            if a not in s:
                s[a] = 0
            if r[0] == 1:
                s[a] += r[3]
            else:
                o[-1] += s[a]
            a //= 2
        elif b != 1:
            if b not in s:
                s[b] = 0
            if r[0] == 1:
                s[b] += r[3]
            else:
                o[-1] += s[b]
            b //= 2
print(*map(str, o), sep='\n')
