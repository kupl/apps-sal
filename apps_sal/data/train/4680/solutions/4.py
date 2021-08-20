from collections import defaultdict
coins = (('H', 50), ('Q', 25), ('D', 10), ('N', 5), ('P', 1))


def make_change(amount):
    result = defaultdict(int)
    for (coin, value) in coins:
        while amount >= value:
            result[coin] += 1
            amount -= value
    return result
