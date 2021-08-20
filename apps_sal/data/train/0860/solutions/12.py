def MinimumHours(n, h, a):
    a.sort()
    pmi = a[-1]
    mi = a[-1]
    s = 0
    while 1:
        for i in a:
            if i % mi == 0:
                s += i // mi
            else:
                s += i // mi + 1
        if s <= h:
            pmi = mi
            mi -= 1
            s = 0
            continue
        return pmi


p = []
for i in range(int(input())):
    (n, h) = input().split()
    p.append(MinimumHours(int(n), int(h), [int(i) for i in input().split()]))
for i in p:
    print(i)
