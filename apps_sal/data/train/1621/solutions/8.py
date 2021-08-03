def count_change(money, coins):
    # your implementation here
    if len(coins) == 1:
        return 1 if money % coins[0] == 0 else 0
    coins = sorted(coins, reverse=True)
    return sum([count_change(money - i * coins[0], coins[1:]) for i in range(money // coins[0] + 1)])
