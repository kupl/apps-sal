def digits_product(product):
    if product < 10:
        return 10 + product
    a = ''
    while product > 1:
        for i in range(9, 1, -1):
            if product % i == 0:
                a += str(i)
                product //= i
                break
        else:
            return -1
    return int(a[::-1])
