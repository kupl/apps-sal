coins = (('H', 50), ('Q', 25), ('D', 10), ('N', 5), ('P', 1))

def make_change(amount):
    result = {}
    for x,y in coins:
        q, amount = divmod(amount, y)
        if q: result[x] = q
        if not amount: return result
