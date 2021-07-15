def excluding_vat_price(price) -> float:
    try:
        return round( price/1.15, 2)
    except TypeError:
        return -1
