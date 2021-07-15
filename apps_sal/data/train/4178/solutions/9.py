def min_sum(arr):
    arr_for_sum = []
    while len(arr) > 0:
        min_elem = min(arr)
        max_elem = max(arr)
        arr_for_sum.append(min_elem * max_elem)
        arr.remove(max_elem)
        arr.remove(min_elem)
    return sum(arr_for_sum)
