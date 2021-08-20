for i in range(int(input())):
    (n, m) = map(int, input().split())
    matrix = []
    for i in range(n):
        row = []
        s = input()
        for i in s:
            row.append(i)
        matrix.append(row)
    ans = 0
    for i in range(m):
        c = 0
        for j in range(n):
            if matrix[j][i] == '1':
                c += 1
        ans += c * (c - 1) // 2
    print(ans)
