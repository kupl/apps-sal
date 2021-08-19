n = int(input())
s = ''
i = 2 * n - 1
sm = 0
if n % 2 == 0:
    print('NO')
elif n == 1:
    print('YES')
    print('1 2')
else:
    a = []
    while i > 2:
        a.append(i)
        a.append(i - 1)
        i -= 4
    a.append(1)
    i = 2 * n
    while i > 2:
        a.append(i)
        a.append(i - 3)
        i -= 4
    a.append(2)
    for i in range(len(a)):
        s += str(a[i])
        s += ' '
    print('YES')
    print(s)
