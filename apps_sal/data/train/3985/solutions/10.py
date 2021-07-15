def find_even_index(arr):
    left, right = 0,sum(arr)
    for i,v in enumerate(arr):
        right -= v
        if left == right: return i
        left += v
    return -1
