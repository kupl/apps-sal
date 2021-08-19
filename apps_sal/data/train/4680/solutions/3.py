def make_change(amount):
    coins = {'H': 50, 'Q': 25, 'D': 10, 'N': 5, 'P': 1}
    change = {}
    for coin in coins:
        if amount >= coins[coin]:
            (change[coin], amount) = divmod(amount, coins[coin])
    return change
