def min_changes(a, n):
    a1 = 0
    b1 = 0
    for i in range(n):
        if (i % 2 == 0):
            if (a[i] == '0'):
                a1 += 1
            else:
                b1 += 1

        else:
            if (a[i] == '0'):
                b1 += 1
            else:
                a1 += 1
    return min(a1, b1)


t = int(input())
while t > 0:
    n = int(input())
    s = input()
    s = list(s)
    print(min_changes(s, n))
    t -= 1
