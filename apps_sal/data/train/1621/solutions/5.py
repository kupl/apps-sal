def count_change(money, coins):
    #
    if money == 0: return 1
    if money < 0: return 0
    if not coins: return 0
    return count_change(money-coins[0], coins) + count_change(money, coins[1:])
