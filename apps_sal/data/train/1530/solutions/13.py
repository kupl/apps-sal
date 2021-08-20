n = int(input())
for i in range(n):
    a = int(input())
    k = 0
    for j in range(1, a + 1):
        k = k + j
        for l in range(k, k - j, -1):
            print(l, end='')
        print()
