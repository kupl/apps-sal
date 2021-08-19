t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    m = int(l[1])
    a = int(l[2])
    b = int(l[3])
    arr = [[0 for i in range(m)] for i in range(n)]
    if n * a != m * b:
        print('NO')
    else:
        diff = 1
        for i in range(n):
            for j in range(a):
                arr[i][(i * a + j) % m] = 1
        print('YES')
        for i in range(n):
            for j in range(m):
                print(arr[i][j], end='')
            print()
