import decimal

def converter(mpg):
    mpg = decimal.Decimal(mpg)
    m2km = decimal.Decimal(1.609344)
    g2l = decimal.Decimal(4.54609188)
    r = mpg * m2km / g2l
    return float(r.quantize(decimal.Decimal("1.00")).normalize())
    # Cmon, having to type beck to float because of assert?
    # This is so broken.

