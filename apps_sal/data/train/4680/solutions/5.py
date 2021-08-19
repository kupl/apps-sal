def make_change(amount):
    coins = {'H': 50, 'Q': 25, 'D': 10, 'N': 5, 'P': 1}
    dict = {}
    for key in coins:
        if amount >= coins[key]:
            (dict[key], amount) = divmod(amount, coins[key])
    return dict
