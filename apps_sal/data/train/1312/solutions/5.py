import sys
t = int(input())
debug = 0
for x in range(t):
    (row, col) = list(map(int, sys.stdin.readline().split()))
    spoon = 0
    matrix = []
    for r in range(row):
        row_in = sys.stdin.readline().strip().lower()
        pos = row_in.find('spoon')
        if pos != -1:
            spoon = 1
        matrix.append(row_in)
    for c in range(col):
        col_in = ''
        for r in range(row):
            col_in += matrix[r][c]
        pos = col_in.find('spoon')
        if pos != -1:
            spoon = 1
    if spoon == 1:
        print('There is a spoon!')
    else:
        print('There is indeed no spoon!')
    if debug == 1:
        print(spoon)
        print(matrix)
