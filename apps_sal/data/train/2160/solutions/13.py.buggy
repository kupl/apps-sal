n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
s = sum(a)
if s % k != 0:
    print("No")
    return
rvl = s // k
vip = []
tvip = 0
tvipl = 0
for cv in range(n):
    tvip += 1
    tvipl += a[cv]
    if tvipl > rvl:
        print("No")
        return
    elif tvipl == rvl:
        vip.append(tvip)
        tvip = 0
        tvipl = 0
print("Yes")
print(*vip, sep=' ')
