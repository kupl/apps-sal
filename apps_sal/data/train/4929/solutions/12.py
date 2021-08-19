def get_diagonale_code(grid: str) -> str:
    flag = True
    temp = grid.split('\n')
    for (i, j) in enumerate(temp):
        temp[i] = j.split()
    res = ''
    x = 0
    y = 0
    while True:
        try:
            res += temp[y][x]
            if y == len(temp) - 1:
                flag = False
            elif y == 0 and (not flag):
                flag = True
            y += 1 if flag else -1
            x += 1
        except:
            return res
