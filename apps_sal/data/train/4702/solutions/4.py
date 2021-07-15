def digits_product(product):

    if product < 10: return 10 + product
    
    lst = []
    for d in range(9, 1, -1):
        while product % d == 0:
            product /= d
            lst.append(d)
    return -1 if product != 1 else int( ''.join(map(str, lst[::-1])) )
