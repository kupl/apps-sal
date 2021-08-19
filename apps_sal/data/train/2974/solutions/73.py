def excluding_vat_price(price):
    try:
        price_ex_vat = round(price / 115 * 100, 2)
    except TypeError:
        return -1
    return price_ex_vat
