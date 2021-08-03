
N, Q = [int(i) for i in input().split()]

row = [0 for i in range(N)]
col = [0 for i in range(N)]

for i in range(Q):
    x = input().split()
    if(x[0] == 'RowAdd'):
        row[int(x[1]) - 1] += int(x[2])
    else:
        col[int(x[1]) - 1] += int(x[2])

print(max(row) + max(col))
