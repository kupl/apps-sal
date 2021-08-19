(k, n) = map(int, input().split())
if k % 2 == 0:
    print(k // 2, end=' ')
    for i in range(n - 1):
        print(k, end=' ')
else:
    l = [(k + 1) // 2 for i in range(n)]
    for i in range(n // 2):
        if l[-1] == 1:
            l.pop()
        else:
            l[-1] -= 1
            for j in range(n - len(l)):
                l.append(k)
    print(*l, sep=' ')
