def excluding_vat_price(price):
    if price is None:
        return -1
    elif price is not None:
        ogprice = 1 / 1.15 * price
        return round(ogprice, 2)
