import collections


def bits(x):
    return bin(x).count('1')


t = int(input())
for _ in range(t):
    q = int(input())
    s = []
    d = collections.defaultdict(lambda: -1)
    e = 0
    o = 0
    p = -1
    for i in range(q):
        x = int(input())
        if d[x] != -1:
            print(e, o)
            continue
        s.append(x)
        d[x] = 1
        for j in s:
            if j != x:
                l = j ^ x
                if d[l] != -1:
                    continue
                s.append(l)
                d[l] = 1
        for j in range(p + 1, len(s)):
            p = j
            if bits(s[j]) % 2 == 0:
                e = e + 1
            elif bits(s[j]) % 2 != 0:
                o = o + 1
        print(e, o)
