
from sys import stdin, stdout
n, q = [int(x) for x in stdin.readline().split()]
row = [0] * n
col = [0] * n
for i in range(q):
    a, b, c = input().split()
    if a == 'RowAdd':
        row[int(b) - 1] += int(c)
    else:
        col[int(b) - 1] += int(c)
print(max(row) + max(col))
