from math import gcd
(n, k) = list(map(int, input().split()))
a = []
for i in range(k):
    try:
        a += list(map(int, input().split()))
    except:
        pass
ans = n
for i in range(1, 2 ** k):
    b = bin(i)[2:].rjust(k, '0')
    c = []
    for j in range(k):
        if b[j] == '1':
            c.append(a[j])
    lcm = c[0]
    for j in c[1:]:
        lcm *= j // gcd(lcm, j)
    temp = (n - 1) // lcm + 1
    if b.count('1') & 1:
        ans -= temp
    else:
        ans += temp
print(ans)
