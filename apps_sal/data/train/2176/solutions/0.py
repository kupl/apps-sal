import heapq

n = int(input())

buy = []  # negative
sell = []
unknown = []

res = 1
for i in range(n):
    cmd, amount = input().strip().split()
    amount = int(amount)
    if cmd == 'ADD':
        if sell and sell[0] < amount:
            heapq.heappush(sell, amount)
        elif buy and -buy[0] > amount:
            heapq.heappush(buy, -amount)
        else:
            unknown.append(amount)
    else:
        if (sell and amount > sell[0]) or (buy and amount < -buy[0]):
            print(0)
            return
        if sell and amount == sell[0]:
            heapq.heappop(sell)
        elif buy and amount == -buy[0]:
            heapq.heappop(buy)
        else:
            res = res * 2 % 1000000007
        for x in unknown:
            if x < amount:
                heapq.heappush(buy, -x)
            elif x > amount:
                heapq.heappush(sell, x)
        unknown = []
res = res * (len(unknown) + 1) % 1000000007
print(res)

