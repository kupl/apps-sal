t = int(input())
for i in range(t):
    k = int(input())
    m = 0
    for j in range(1, k + 1):
        for m in range(1, k + 1):
            if j == k:
                print('*', end='')
            elif m == 1 or m == j:
                print('*', end='')
            else:
                print(' ', end='')
        print()
