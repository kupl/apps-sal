import heapq

n = int(input())

ans = 1

mod = 10**9 + 7

buy, undefined, sell = [], [], []

for i in range(n):
    cmd, str_p = input().split()
    p = int(str_p)

    if cmd == 'ADD':
        if buy and p < -buy[0]:
            heapq.heappush(buy, -p)
        elif sell and p > sell[0]:
            heapq.heappush(sell, p)
        else:
            undefined.append(p)
    else:
        if (buy and p < -buy[0]) or (sell and p > sell[0]):
            ans = 0
            break
        elif buy and p == -buy[0]:
            heapq.heappop(buy)
        elif sell and p == sell[0]:
            heapq.heappop(sell)
        else:
            ans = (ans << 1) % mod
        for x in undefined:
            if x < p:
                heapq.heappush(buy, -x)
            elif x > p:
                heapq.heappush(sell, x)
        undefined = []

ans = ans * (len(undefined) + 1) % mod

print(ans)
