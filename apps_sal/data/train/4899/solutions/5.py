import decimal


def weight(n, w):
    I0 = decimal.Decimal(0.14849853757254047)
    OFFSET = decimal.Decimal(7.389056098930639)
    return float((OFFSET - (1 / OFFSET ** n)) / (OFFSET - 1) * w * I0)
