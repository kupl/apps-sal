n = int(input())
if n % 2:
    print('YES')
    a = [0] * (n * 2)
    for i in range(n):
        if i % 2:
            a[i] = i * 2 + 2
            a[i + n] = i * 2 + 1
        else:
            a[i] = i * 2 + 1
            a[i + n] = i * 2 + 2
    print(' '.join(map(str, a)))
else:
    print('NO')
