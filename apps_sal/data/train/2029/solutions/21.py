n = int(input())
if not n % 2:
    print('NO')
else:
    lower = [i for i in range(1, 2 * n, 2)]
    upper = [i for i in range(2, 2 * n + 1, 2)]
    circle = []
    append = circle.append
    for i in range(n):
        append(lower[i] if i % 2 else upper[i])
    for i in range(n):
        append(upper[i] if i % 2 else lower[i])
    print('YES')
    print(' '.join(map(str, circle)))
