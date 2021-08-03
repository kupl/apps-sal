n = int(input())
if not n % 2:
    print('NO')
else:
    print('YES')
    print(1, end=' ')
    for i in range(4, 2 * n, 4):
        print(i, i + 1, end=' ')
    for i in range(2, 2 * n, 4):
        print(i, i + 1, end=' ')
    print(2 * n)
