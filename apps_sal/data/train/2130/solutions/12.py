def com(lo, hi):
    loo = 1
    for i in range(1, lo + 1):
        loo *= i
    hii = 1
    for i in range(hi, hi - lo, -1):
        hii *= i
    return hii // loo


n = int(input())
data = [int(input()) for i in range(n)]
ans = 1
total = sum(data)
for i in range(len(data) - 1, -1, -1):
    ans *= com(data[i] - 1, total - 1)
    total -= data[i]
print(ans if ans < 1000000007 else ans % 1000000007)
