def adjacent_element_product(arr):
    product = [arr[i]*arr[i+1] for i in range(len(arr)-1)]
    print (product)
    return max(product)
