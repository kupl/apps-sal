def mango(quantity, price):
    buy = 0
    bill = 0
    while buy < quantity:
        buy += 3
        bill += price * 2

    if buy == quantity:
        return bill
    elif buy - quantity == 1:
        return bill
    elif buy - quantity == 2:
        return bill - price
