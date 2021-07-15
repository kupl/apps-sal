n = int(input())
a = list(map(int, list(input())))
b = list(map(int, list(input())))
a0 = 0
a1 = 0
ans = 0
b0 = 0
b1 = 0
for i in a:
    if i == 0:
        a0 += 1
    else:
        a1 += 1
for i in range(n):
    if b[i] == 0:
        if a[i] == 0:
            ans += a1
            b0 += 1
        else:
            ans += a0
            b1 += 1
ans -= b0 * b1
print(ans)

