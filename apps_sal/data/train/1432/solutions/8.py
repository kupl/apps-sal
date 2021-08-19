t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        lis = [int(inp) for inp in input().split()]
        a.append(lis)
    zer_count = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                zer_count += 1
    count = 0
    while count <= n:
        zer_count -= 2 * (count + 1)
        if zer_count < 0:
            break
        else:
            count += 1
    print(n - 1 - count)
