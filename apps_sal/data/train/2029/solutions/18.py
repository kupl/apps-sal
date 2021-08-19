n = int(input())
if n % 2 == 0:
    print('NO')
else:
    print('YES')
    d = 1
    for i in range(n):
        print(d, end=' ')
        d += 3 if i % 2 == 0 else 1
    d = 2
    for i in range(n):
        print(d, end=' ')
        d += 1 if i % 2 == 0 else 3
