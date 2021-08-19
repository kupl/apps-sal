def product_array(numbers):
    prod = eval('*'.join(map(str, numbers)))
    return [prod / x for x in numbers]
