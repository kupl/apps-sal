def lcs(A, B):
    a, b = len(A), len(B)
    lst = [[0] * (b + 1) for _ in range(a + 1)]
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if A[x - 1] == B[y - 1]:
                lst[x][y] = 1 + lst[x - 1][y - 1]
            else:
                lst[x][y] = max(lst[x][y - 1], lst[x - 1][y])
    return lst[a][b]


for _ in range(int(input())):
    n = int(input())
    lst = []
    for i in range(n):
        stg = input()
        m = len(stg)
        lst.append(min(lcs(stg, m * 'a'), lcs(stg, m * 'b')))
    print(min(lst))
