n = int(input())
if n%4 > 1:
    print(-1)
    return
a = [(n+1) // 2] * n
for i in range(n//4):
    j = 2*i
    a[j], a[j+1], a[-j-2], a[-j-1] = j+2, n-j, j+1, n-j-1
print(' '.join(map(str, a)))

