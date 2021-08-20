for _ in range(int(input())):
    (r, c) = map(int, input().split())
    board = []
    for i in range(r):
        x = input()
        board.append(x)
    coll = []
    for i in range(r):
        coll.append([])
        for j in range(c):
            coll[i].append([])
    for i in range(r):
        for j in range(c):
            if board[i][j] == '-' or board[i][j] == '#':
                pass
            else:
                cnt = 1
                if board[i][j] == 'D':
                    for k in range(i + 1, r):
                        if board[k][j] == '#':
                            break
                        coll[k][j].append(cnt)
                        cnt += 1
                if board[i][j] == 'U':
                    for k in range(i - 1, -1, -1):
                        if board[k][j] == '#':
                            break
                        coll[k][j].append(cnt)
                        cnt += 1
                if board[i][j] == 'R':
                    for k in range(j + 1, c):
                        if board[i][k] == '#':
                            break
                        coll[i][k].append(cnt)
                        cnt += 1
                if board[i][j] == 'L':
                    for k in range(j - 1, -1, -1):
                        if board[i][k] == '#':
                            break
                        coll[i][k].append(cnt)
                        cnt += 1
    cnts = 0
    for i in range(r):
        for j in range(c):
            if len(coll[i][j]) > 1:
                sets = set(coll[i][j])
                counts = {}
                for k in sets:
                    counts[k] = 0
                for k in coll[i][j]:
                    counts[k] += 1
                for k in counts.values():
                    if k > 1:
                        cnts += int(k * (k - 1) // 2)
    print(cnts)
