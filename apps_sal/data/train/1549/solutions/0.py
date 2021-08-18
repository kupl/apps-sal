import copy
for _ in range(int(input())):
    k = int(input())
    c = []
    d = []
    start = 0

    while True:
        c = []
        for i in range(start):
            c.append(" ")
        for i in range(start, k + 1):
            c.append(str(i))
        start += 1
        d.append(c)

        if start > k:
            break

    e = copy.copy(d[1:])
    d.reverse()
    d = d + e
    for i in range(len(d)):
        print(''.join(d[i]))
