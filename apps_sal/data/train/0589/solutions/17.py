t = int(input())


def attic(s):
    c = 0
    l = []
    k = 0
    m = 0
    for i in range(len(p)):
        if s[i] == '.':
            c += 1
        else:
            if c > k:
                k = c
                m += 1
                l.append(c)

            c = 0
    return m


for _ in range(t):
    p = input()
    r = attic(p)
    print(r)
