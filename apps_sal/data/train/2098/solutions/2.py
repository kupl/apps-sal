n, m = map(int, input().split())  # voters, parties

money = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    money[i] = (y, x - 1)

money.sort()


def calc(lim):
    visited = [False] * n
    cost = 0

    cnt = [0] * m
    for i in range(n):
        cnt[money[i][1]] += 1

    for i in range(n):
        if money[i][1] != 0 and cnt[money[i][1]] >= lim:
            cnt[money[i][1]] -= 1
            cnt[0] += 1
            cost += money[i][0]
            visited[i] = True

    for i in range(n):
        if cnt[0] >= lim:
            break

        if money[i][1] != 0 and not visited[i]:
            cnt[money[i][1]] -= 1
            cnt[0] += 1
            cost += money[i][0]

    return cost


ans = 10 ** 18

for i in range(n):
    ans = min(ans, calc(i))

print(ans)
