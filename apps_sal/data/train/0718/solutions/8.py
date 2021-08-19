t = int(input())
for _ in range(t):
    n = int(input())
    a = 1
    b = 2
    for i in range(n):
        for j in range(i + 1):
            if i == 0:
                print('0', end=' ')
            elif i == 1:
                print('1', end=' ')
            else:
                print(b, end=' ')
                c = b
                b = a + b
                a = c
        print()
