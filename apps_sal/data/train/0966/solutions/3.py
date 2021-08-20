t = int(input())
for _ in range(t):
    (n, u, d) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    c = 1
    j = 1
    for i in range(n - 1):
        if a[i] >= a[i + 1]:
            if abs(a[i] - a[i + 1]) <= d:
                c += 1
            elif j == 1:
                c += 1
                j = 0
            else:
                break
        elif a[i] < a[i + 1]:
            if abs(a[i] - a[i + 1]) <= u:
                c += 1
            else:
                break
    print(c)
