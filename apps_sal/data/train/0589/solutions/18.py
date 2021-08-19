t = int(input())


def attic(s):
    c = 0
    l = []
    k = 0
    for i in range(len(p)):
        if s[i] == '.':
            c += 1
        else:
            if c > k:
                k = c
                l.append(c)
            c = 0
    return len(set(sorted(l)))


for _ in range(t):
    p = input()
    r = attic(p)
    print(r)
