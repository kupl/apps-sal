def count_change(money, coins):
    (_, coin, rest) = (coins.sort(reverse=True), coins[0], coins[1:])
    if not rest:
        return int(not money % coin)
    return sum((count_change(money - i, rest) for i in range(0, money + 1, coin)))
