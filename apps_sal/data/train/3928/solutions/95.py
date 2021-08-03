def billboard(name, price=30):
    amount = 0
    for _ in name:
        amount += price
    return amount
