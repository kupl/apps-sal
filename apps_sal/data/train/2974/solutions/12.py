def excluding_vat_price(n):
    return -(not n) or round(n / 1.15, 2)
