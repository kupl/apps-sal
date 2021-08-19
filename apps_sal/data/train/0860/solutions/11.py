# cook your dish here
def MinimumHours(n, h, a):
    a.sort()
    j = 0
    mi = a[j]
    s = 0
    c = 0
    c2 = 0
    while 1:
        for i in a[-1:-(n + 2):-1]:
            if i % mi == 0:
                s += (i // mi)
            else:
                s += (i // mi) + 1
            if s > h:
                c = 1
                if c2 == 1:
                    return mi + 1
                break
        if c2 == 0 and c == 1:
            pmi = mi
            j += 1
            mi = a[j]
            c = 0
            s = 0
            continue
        c2 = 1
        mi -= 1
        s = 0


p = []
for i in range(int(input())):
    n, h = input().split()
    p.append(MinimumHours(int(n), int(h), [int(i) for i in input().split()]))

for i in p:
    print(i)
