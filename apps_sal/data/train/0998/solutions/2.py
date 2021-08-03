n, q = list(map(int, input().split()))
row = [0] * n
column = [0] * n
for i in range(q):
    a, b, c = input().split()
    if a == 'RowAdd':
        row[int(b) - 1] += int(c)
    else:
        column[int(b) - 1] += int(c)
print(max(row) + max(column))
