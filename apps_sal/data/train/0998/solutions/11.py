(n, q) = map(int, input().split())
a = [0] * n
b = [0] * n
while q > 0:
    (o, r, v) = input().split()
    if o == 'RowAdd':
        a[int(r) - 1] += int(v)
    else:
        b[int(r) - 1] += int(v)
    q = q - 1
print(max(a) + max(b))
