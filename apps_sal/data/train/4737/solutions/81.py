def fuel_price(l, p):
    return l * p - l * min(.25, (l // 2) * 5 * .01)
