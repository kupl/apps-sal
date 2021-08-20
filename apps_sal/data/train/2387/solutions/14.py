t = int(input())
for _ in range(t):
    s = int(input())
    ans = 0
    while s >= 10:
        to_spend = s // 10 * 10
        ans += to_spend
        s -= to_spend
        s += to_spend // 10
    ans += s
    print(ans)
