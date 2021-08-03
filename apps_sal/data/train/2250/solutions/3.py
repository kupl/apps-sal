__author__ = 'Think'
n, m, k = [int(i) for i in input().split()]
n = 2 * n
m = 2 * m
a, b = sorted((m, n))
tracker = [b]

while a > 0:
    b = (b % a)
    tracker.append(a)
    a, b = (b, a)

g = b
prod = (m * n) // g

if m != n:
    if len(tracker) >= 3:
        pair = (1, -(tracker[-3] // tracker[-2]))
        for i in range(len(tracker) - 4, -1, -1):
            new = -(tracker[i] // tracker[i + 1])
            pair = (pair[1], pair[0] + pair[1] * new)

        if sorted((m, n))[0] == n:
            pair = (pair[1], pair[0])
        a, b = pair
    else:
        if m > n:
            a = 1
            b = 0
        else:
            a = 0
            b = 1

    for i in range(k):
        x, y = [int(i) for i in input().split()]
        if (x - y) % g != 0 and (x + y) % g != 0:
            print(-1)
            continue
        else:
            shortlist = []
            for nx in [x, -x]:
                if ((nx - y) % g) == 0:
                    new = (nx + a * n * ((y - nx) // g)) % prod
                    shortlist.append(new)
                    shortlist.append(prod - new)
            if len(shortlist) > 0:
                print(min(shortlist))
            else:
                print(-1)
else:
    for i in range(k):
        x, y = [int(i) for i in input().split()]
        if x != y:
            print(-1)
        else:
            print(x)
