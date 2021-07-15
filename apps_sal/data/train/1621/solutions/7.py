def count_change(money, coins):
    if len(coins) == 0 or money < 0:
        return 0
    if money == 0:
        return 1
    return count_change(money - coins[0], coins) + count_change(money, coins[1:])
