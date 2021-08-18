T = int(input())

while T > 0:
    R, C = input().split()
    R = int(R)
    C = int(C)
    output = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            output[i][j] = dict()
    matrix = [0] * R
    for i in range(R):
        matrix[i] = input()
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 'R':
                column = j + 1
                while column < C and matrix[i][column] != '
                output[i][column][column - j] = output[i][column].get(column - j, 0) + 1
                column = column + 1
            elif matrix[i][j] == 'L':
                column = j - 1
                while column >= 0 and matrix[i][column] != '
                output[i][column][j - column] = output[i][column].get(j - column, 0) + 1
                column = column - 1
            elif matrix[i][j] == 'U':
                row = i - 1
                while row >= 0 and matrix[row][j] != '
                output[row][j][i - row] = output[row][j].get(i - row, 0) + 1
                row = row - 1
            elif matrix[i][j] == 'D':
                row = i + 1
                while row < R and matrix[row][j] != '
                output[row][j][row - i] = output[row][j].get(row - i, 0) + 1
                row = row + 1
    no_of_pairs = 0
    for i in range(R):
        for j in range(C):
            for no_of_steps, count in output[i][j].items():
                if count > 1:
                    no_of_pairs = no_of_pairs + (count * (count - 1)) // 2
    print(no_of_pairs)
    T = T - 1
