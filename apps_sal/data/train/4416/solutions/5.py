def loose_change(cents):
    cents = max(cents, 0)
    d = {}
    for (coin, n) in (('Quarters', 25), ('Dimes', 10), ('Nickels', 5), ('Pennies', 1)):
        (d[coin], cents) = divmod(cents, n)
    return d
