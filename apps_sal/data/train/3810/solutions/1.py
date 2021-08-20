def product(list):
    p = 1
    for i in list:
        p *= int(i)
    return p


def greatest_product(list):
    res = []
    mul = 1
    while len(list) >= 5:
        res.append(product(list[:5]))
        list = list[1:]
    return max(res)
