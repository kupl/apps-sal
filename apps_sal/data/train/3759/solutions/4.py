def product_array(n):
    prod = eval("*".join(map(str, n)))
    return [prod // i for i in n]
