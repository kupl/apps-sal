def count(board):
    cnt = [0] * (len(board) + 1)
    scan = [0] * (len(board) + 1)
    for row in board:
        (prev, scan) = (scan, [0])
        for (n, b) in enumerate(row):
            scan.append(b and min(prev[n], prev[n + 1], scan[n]) + 1)
        for x in scan:
            cnt[x] += 1
    ans = {}
    for x in range(len(cnt) - 1, 1, -1):
        if not cnt[x]:
            continue
        ans[x] = cnt[x]
        cnt[x - 1] += cnt[x]
    return ans
