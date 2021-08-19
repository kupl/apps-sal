def matrixScore(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    (m, n) = (len(A), len(A[0]))
    for i in range(m):
        if A[i][0] == 1:
            continue
        for j in range(n):
            A[i][j] = 1 - A[i][j]
    res = 0
    for rows in zip(*A):
        cnt1 = max(rows.count(1), rows.count(0))
        res += cnt1 * 2 ** (n - 1)
        n -= 1
    return res


(m, n) = [int(s) for s in input().split(' ')]
arr = [[int(s) for s in input().split(' ')] for i in range(m)]
ans = matrixScore(arr)
print(ans)
