def find_even_index(arr):
    right = sum(arr)
    left = 0
    for i, x in enumerate(arr):
        right -= x
        if right == left:
            return i
        left += x
    return -1
