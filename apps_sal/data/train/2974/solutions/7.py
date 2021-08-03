def excluding_vat_price(price):
    return float('%.2f' % (price / 115 * 100)) if price else -1
