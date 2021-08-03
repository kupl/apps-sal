def count_change(money, coins):
    results = [0] * (money + 1)
    results[0] = 1
    for i in coins:
        for j in range(i, money + 1):
            results[j] += results[j - i]
    return results[money]
