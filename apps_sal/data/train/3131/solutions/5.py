def unique_digit_products(a):
    return len({eval('*'.join(str(n))) for n in a})
