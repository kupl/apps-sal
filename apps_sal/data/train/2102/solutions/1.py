k = int(input())
p = [['0'] * 100 for i in range(100)]
j = n = 0
while j < k:
    for i in range(n):
        if j + i > k:
            break
        p[n][i] = p[i][n] = '1'
        j += i
    n += 1
print(n)
for i in range(n):
    print(''.join(p[i][:n]))
