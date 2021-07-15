def magic_sum(arr):
    if arr == None: return 0 
    return sum(list(filter(lambda x: x % 2 == 1 and '3' in str(x),arr)))
