n = int(input())
if n % 2 == 0:
    print('NO')
else:
    print('YES')
    l = [0 for i in range(2 * n)]
    for i in range(n):
        if i % 2 == 0:
            l[i] = i * 2 + 1
            l[i + n] = l[i] + 1
        else:
            l[i] = i * 2 + 2
            l[i + n] = l[i] - 1
    print(*l)
