try:
    for _ in range(int(input())):
        row, column = list(map(int, input().split(" ")))
        x_x, y_y = list(map(int, input().split(" ")))
        ab = max((x_x - 0), (row - x_x - 1))
        ba = max((y_y - 0), (column - y_y - 1))
        print(ab + ba)
except:
    pass
