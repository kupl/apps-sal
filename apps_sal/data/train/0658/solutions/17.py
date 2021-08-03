def check(b):

    ch = True

    for m in range(len(b) - 1):
        if m % 2 == 0:
            if b[m] > b[m + 1]:
                ch = False
        else:
            if b[m] < b[m + 1]:
                ch = False

    return ch


def big(n, a):
    maxi = 1
    c = []

    for j in range(len(a)):
        for l in range(j + 1, len(a)):
            if check(a[j:l + 1]) == True:
                if len(a[j:l + 1]) > maxi:
                    maxi = len(a[j:l + 1])
                    c = a[j:l + 1]

    return maxi, c


t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    final_max = 0

    e = a[:]
    e.insert(0, a[0] + 1)
    if len(big(n, e)[1]) > final_max:
        final_max = len(big(n, e)[1])

    e = a[:]
    e.insert(0, a[0] + 1)
    if len(big(n, e)[1]) > final_max:
        final_max = len(big(n, e)[1])

    e = a[:]
    e.insert(len(a), a[len(a) - 1] - 1)
    if len(big(n, e)[1]) > final_max:
        final_max = len(big(n, e)[1])

    e = a[:]
    e.insert(len(a), a[len(a) - 1] + 1)
    if len(big(n, e)[1]) > final_max:
        final_max = len(big(n, e)[1])

    for l in range(1, len(a)):
        d = a[:]
        bef, aft = a[l - 1], a[l]
        if bef > aft:
            d.insert(l, bef + 1)
        else:
            d.insert(l, bef - 1)
        maxi, c = big(l, d)
        if len(c) > final_max:
            final_max = len(c)
    print(final_max)
