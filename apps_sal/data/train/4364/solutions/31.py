def odd_or_even(arr):
    if len(arr) == 0:
        return [0]
    
    val = sum(arr)
    
    if val % 2 == 0:
        return"even"
    else:
        return "odd"
