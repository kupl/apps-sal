t = int(input())
for i in range(0, t):
    n = int(input())
    for j in range(2, n + 2):
        for k in range(j, n + j):
            print(k, end='')
        print(' ')
