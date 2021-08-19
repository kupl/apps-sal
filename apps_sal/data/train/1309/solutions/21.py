n = int(input())
for i in range(n):
    a = int(input())
    for j in range(a, 0, -1):
        for k in range(a - j):
            print('*', end='')
        for k in range(j, 0, -1):
            print(k, end='')
        print()
