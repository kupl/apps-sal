# cook your dish here
from sys import stdin, stdout
rows, columns = map(int, stdin.readline().strip().split())
matrix = []
for _ in range(rows):
    row = list(map(int, stdin.readline().strip().split()))
    matrix.append(row)
C = int(stdin.readline().strip())
for _ in range(C):
    tlx, tly, brx, bry = map(int, stdin.readline().strip().split())
    s = 0
    for r in range(tlx - 1, brx):
        for c in range(tly - 1, bry):
            s += matrix[r][c]
    stdout.write(str(s) + '\n')
