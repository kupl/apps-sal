n = int(input())
p = 0 if n <= 100 else n - 100
ans = []
while p <= n:
    k = p
    s = p
    while k > 0:
        s += k % 10
        k = k // 10
    if s == n:
        ans.append(p)
    p += 1
if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    for i in ans:
        print(i)
