from numpy import prod
def product_array(numbers):
    return [prod(numbers)/i for i in numbers]
