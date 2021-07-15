adjacent_element_product = lambda arr: len(arr) and max(x*y for x,y in zip(arr, arr[1:]))
