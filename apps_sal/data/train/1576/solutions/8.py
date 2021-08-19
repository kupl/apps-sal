t = int(input())
for i in range(t):
    k = int(input())
    m = 0
    for j in range(1, k + 1):
        for m in range(j, k + 1):
            print(m, end='')
        for n in range(1, j):
            print(n, end='')
        print()
