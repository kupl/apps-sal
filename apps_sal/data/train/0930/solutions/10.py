

for _ in range(int(input())):
    n = int(input())
    l = [[0 for i in range(n)] for j in range(n)]
    c = 1
    cur = 0
    while(1):
        i = 0
        j = cur
        while(j >= 0):
            l[i][j] = c
            c += 1
            j -= 1
            i += 1
        cur += 1
        if cur == n:
            break

    cur = n - 1
    curi = 1
    while(1):
        i = curi
        j = cur
        if curi == n:
            break
        while(i != n):
            l[i][j] = c
            c += 1
            i += 1
            j -= 1
        curi += 1

    for i in range(n):
        for j in range(n):
            print(l[i][j], end=" ")
        print()
