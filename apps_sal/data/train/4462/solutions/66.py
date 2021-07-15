def adjacent_element_product(arr):
    return max([ e1*e2 for e1,e2 in zip(arr[1:] , arr[:-1])])
