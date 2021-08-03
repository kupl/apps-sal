from math import ceil


def pay_cheese(a):
    return f"L{round(ceil(((sum(a)*6.)/10.)/60.)*35)}"
