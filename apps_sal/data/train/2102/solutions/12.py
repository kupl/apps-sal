(n, k) = (0, int(input()))
p = [['0'] * 100 for i in range(100)]
while k:
    for i in range(n):
        if i > k:
            break
        p[n][i] = p[i][n] = '1'
        k = k - i
    n += 1
print(n)
for i in range(n):
    print(''.join(p[i][:n]))
