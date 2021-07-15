from functools import reduce
def product_array(numbers):
    r = lambda x, y: x * y
    return [reduce(r, (x for i, x in enumerate(numbers) if i != index)) for index in range(len(numbers))]
