def loose_change(cents):
    res = {}
    (res['Quarters'], cents) = divmod(cents, 25) if cents > 0 else (0, 0)
    (res['Dimes'], cents) = divmod(cents, 10)
    (res['Nickels'], cents) = divmod(cents, 5)
    (res['Pennies'], cents) = divmod(cents, 1)
    return res
