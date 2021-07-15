n = int(input())
money = list(map(int, input().split()))
k = int(input())
f = len(money) - k
ans = curr = sum(money[:f])
for i in range(f, len(money)):
    curr += money[i] - money[i - f]
    ans = min(ans, curr)
print(sum(money) - ans)
