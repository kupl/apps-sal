def max_size(mat, ZERO=0):
    nrows, ncols = len(mat), (len(mat[0]) if mat else 0)
    if not (nrows and ncols):
        return 0
    counts = [[0] * ncols for _ in range(nrows)]
    for i in reversed(range(nrows)):
        assert len(mat[i]) == ncols
        for j in reversed(range(ncols)):
            if mat[i][j] != ZERO:
                counts[i][j] = (1 + min(
                    counts[i][j + 1],
                    counts[i + 1][j],
                    counts[i + 1][j + 1]
                )) if i < (nrows - 1) and j < (ncols - 1) else 1
    return max(c for rows in counts for c in rows)


l, r, k = list(map(int, input().split()))
a, ans = [], ['no', 'yes']
for _ in range(0, l):
    q = input().replace('M', '1').replace('F', '0')
    a.append(list(map(int, list(q))))
f = max_size(a, 1)
m = max_size(a, 0)
for _ in range(0, k):
    n, q = input().split()
    if q == 'M':
        print(ans[int(n) <= m])
    else:
        print(ans[int(n) <= f])
