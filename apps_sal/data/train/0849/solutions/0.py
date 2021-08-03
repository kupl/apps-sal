n = eval(input())
a = list(map(int, input().split()))
c = m = 0
maxi = max(a)
for i in range(n):
    if a[i] == maxi:
        c += 1
        m = max(c, m)
    else:
        c = 0
print(m)
