def mango(quantity, price):
    deal = int(quantity / 3)
    no_deal = quantity - deal * 3
    return deal * 2 * price + no_deal * price
