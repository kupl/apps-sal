def count(board):
    (cnt, scan) = ({}, [0] * (len(board) + 1))
    for row in board:
        (prev, scan) = (scan, [0])
        for (n, b) in enumerate(row):
            scan.append(b and min(prev[n], prev[n + 1], scan[n]) + 1)
        for x in scan:
            if x > 1:
                cnt[x] = cnt.get(x, 0) + 1
    for x in range(max(cnt, default=2), 2, -1):
        cnt[x - 1] += cnt[x]
    return cnt
