"""input
2
7 3 5
5 2 5 2
2 4 2 6
6 2 6 4
5 6 5 7
7 1 7 4
7 3 7
1 1 6 1
1 2 3 2
5 2 5 2
2 6 2 6
6 2 6 4
5 6 5 7
7 1 7 4
"""
for _ in range(int(input())):
    (n, k, m) = list(map(int, input().split()))
    row_s = []
    col_s = []
    for _ in range(m):
        (h_x, h_y, t_x, t_y) = list(map(int, input().split()))
        if h_x == t_x:
            if h_x < (n - k) // 2 + 1 or h_x > (n - k) // 2 + k:
                col_s.append([min(h_y, t_y), max(h_y, t_y)])
            else:
                row_s.append([h_x, h_x])
        if h_y == t_y:
            if h_y < (n - k) // 2 + 1 or h_y > (n - k) // 2 + k:
                row_s.append([min(h_x, t_x), max(h_x, t_x)])
            else:
                col_s.append([h_y, h_y])
    row_s.sort()
    col_s.sort()
    poss = True
    if len(col_s) == 0 or len(row_s) == 0:
        print(-1)
        continue
    next_row = (n - k) // 2 + 1
    i = 0
    count_row = 0
    while i < len(row_s):
        max_next = next_row
        if next_row < row_s[i][0]:
            poss = False
            break
        while i < len(row_s) and row_s[i][0] <= next_row:
            max_next = max(max_next, row_s[i][1] + 1)
            i += 1
        next_row = max_next
        count_row += 1
        if next_row > (n - k) // 2 + k:
            break
        if next_row < (n - k) // 2 + k and i >= len(row_s):
            poss = False
            break
    next_col = (n - k) // 2 + 1
    i = 0
    count_col = 0
    while i < len(col_s):
        max_next = next_col
        if next_col < col_s[i][0]:
            poss = False
            break
        while i < len(col_s) and col_s[i][0] <= next_col:
            max_next = max(max_next, col_s[i][1] + 1)
            i += 1
        next_col = max_next
        count_col += 1
        if next_col > (n - k) // 2 + k:
            break
        if next_col < (n - k) // 2 + k and i >= len(col_s):
            poss = False
            break
    print(count_col + count_row if poss else -1)
