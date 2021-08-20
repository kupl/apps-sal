q = int(input())
for _ in range(q):
    n = int(input())
    row1 = input()
    row2 = input()
    pos = (0, 0)
    turn = '3456'
    straight = '12'
    while pos != (1, n) and pos[1] < n:
        if pos[0] == 0:
            if row1[pos[1]] in turn:
                if row2[pos[1]] in turn:
                    pos = (1, pos[1] + 1)
                else:
                    break
            else:
                pos = (0, pos[1] + 1)
        elif pos[0] == 1:
            if row2[pos[1]] in turn:
                if row1[pos[1]] in turn:
                    pos = (0, pos[1] + 1)
                else:
                    break
            else:
                pos = (1, pos[1] + 1)
    if pos == (1, n):
        print('YES')
    else:
        print('NO')
