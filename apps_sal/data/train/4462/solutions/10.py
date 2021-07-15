def adjacent_element_product(lst):
    return max(lst[i]*lst[i+1] for i in range(len(lst)-1))
