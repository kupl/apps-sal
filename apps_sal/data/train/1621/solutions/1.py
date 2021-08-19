def count_change(money, coins):
    ways = [1] + [0] * (money + 1)
    for coin in coins:
        for i in range(coin, money + 1):
            ways[i] += ways[i - coin]
    return ways[money]
