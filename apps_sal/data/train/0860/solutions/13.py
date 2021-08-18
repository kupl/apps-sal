def MinimumHours(n, h, a):
    a.sort()
    j = 0
    mie = 2
    mio = 1
    s1 = 0
    s2 = 0
    c1 = 0
    c2 = 0
    while 1:
        for i in a[-1:-(n + 1):-1]:
            if i % mie == 0:
                s1 += (i // mie)
            else:
                s1 += (i // mie) + 1
            if i % mio == 0:
                s2 += (i // mio)
            else:
                s2 += (i // mio) + 1
            if s1 > h:
                c1 = 1

            if s2 > h:
                c2 = 1
            if c1 == c2 == 1:
                break

        if c1 == c2 == 1:
            c1 = 0
            s1 = 0
            c2 = 0
            s2 = 0
            mie += 2
            mio += 2
        else:
            if c2 == c1 == 0:
                return min(mie, mio)
            if c1 == 0:
                return mie
            return mio


p = []
for i in range(int(input())):
    n, h = input().split()
    p.append(MinimumHours(int(n), int(h), [int(i) for i in input().split()]))

for i in p:
    print(i)
