for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort(reverse=True)
    c = l[0] + l[1]
    for i in range(2, n):
        c += l[i] * 2 ** (i - 1)
    c /= 2 ** (n - 1)
    print(format(c, '.8f'))
