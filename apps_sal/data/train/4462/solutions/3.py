from operator import mul
def adjacent_element_product(array):
    return max(map(mul, array, array[1:]))
