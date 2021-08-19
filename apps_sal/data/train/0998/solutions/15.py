(n, m) = list(map(int, input().split()))
a = [0] * (n + 1)
b = [0] * (n + 1)
for i in range(0, m):
    op = input().split()
    if op[0] == 'RowAdd':
        a[int(op[1])] += int(op[2])
    if op[0] == 'ColAdd':
        b[int(op[1])] += int(op[2])
print(max(a) + max(b))
