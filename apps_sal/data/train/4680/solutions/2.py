COINS = dict(H=50, Q=25, D=10, N=5, P=1)


def make_change(amount):
    result = {}
    for coin, value in COINS.items():
        if amount >= value:
            result[coin], amount = divmod(amount, value)
    return result
