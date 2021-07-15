n = int(input())
if n == 2:
    print('1\n1 1')
elif n == 1:
    print('1\n1')
else:
    a = [True for i in range(n + 2)]
    for i in range(2, n + 2):
        if a[i]:
            for j in range(i * 2, n + 2, i):
                a[j] = False
    print(2, 1, sep = '\n', end = '')
    for i in range(1, n):
        print('', 2 - a[i + 2], end = '')

