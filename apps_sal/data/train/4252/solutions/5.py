def merge_arrays(first, second): 
    # your code here
    first.extend(second)
    x = list(set(first))
    x.sort()
    return x
