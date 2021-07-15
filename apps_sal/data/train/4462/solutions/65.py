def adjacent_element_product(a):
#     return max([x*y for x in a[:-1] for y in a[1:] ])
    return max([a[i]*a[i+1] for i in range(0,len(a)-1)])
