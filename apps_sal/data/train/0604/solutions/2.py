def adjacent(i, j, r, c):
    if i == 0 or i == r - 1:
        if j == 0 or j == c - 1:
            return 2
        else:
            return 3
    elif j == 0 or j == c - 1:
        return 3
    else:
        return 4


for _ in range(int(input())):
    (r, c) = map(int, input().split(' '))
    grid = []
    flag = 0
    for i in range(r):
        grid.append(list(map(int, input().split(' '))))
    for i in range(r):
        for j in range(c):
            if adjacent(i, j, r, c) <= grid[i][j]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        print('Unstable')
    else:
        print('Stable')
