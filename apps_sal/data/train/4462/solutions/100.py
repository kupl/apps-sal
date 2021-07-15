def adjacent_element_product(array):
    maxp = float('-inf')
    for i in range(1, len(array)):
        x = array[i]
        y = array[i-1]
        maxp = max(maxp, x*y)
    return maxp
