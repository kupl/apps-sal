def find_2nd_largest(arr): 
    newarr = sorted(list({x for x in arr if type(x) == int})) # remove duplicates and non-int objects, sort
    return newarr[-2] if len(newarr) > 1 else None
