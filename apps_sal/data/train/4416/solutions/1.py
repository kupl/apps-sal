CHANGES = (('Quarters', 25),
           ('Dimes', 10),
           ('Nickels', 5),
           ('Pennies', 1))


def loose_change(cents):
    cents, changed = max(0, int(cents)), {}
    for what, value in CHANGES:
        n, cents = divmod(cents, value)
        changed[what] = n
    return changed
