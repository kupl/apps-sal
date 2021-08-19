for _ in range(int(input())):
    n = int(input())
    x = []
    y = []
    k = 4 * n - 1
    for i in range(k):
        (a, b) = input().split()
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    l = y[k - 1]
    j = x[k - 1]
    for i in range(0, k - 1, 2):
        if x[i] != x[i + 1]:
            j = x[i]
            break
    for i in range(0, k - 1, 2):
        if y[i] != y[i + 1]:
            l = y[i]
            break
    print(j, l)
