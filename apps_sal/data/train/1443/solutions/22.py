for _ in range(int(input())):
    (n, m) = map(int, input().split())
    matrix = []
    for i in range(n):
        row = []
        s = input()
        for ele in s:
            row.append(ele)
        matrix.append(row)
    ans = 0
    for i in range(m):
        cnt = 0
        for j in range(n):
            if matrix[j][i] == '1':
                cnt += 1
        ans += cnt * (cnt - 1) // 2
    print(ans)
