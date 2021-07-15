def remove_smallest(numbers):
    arr = numbers.copy()
    if arr == []:
        return []
    else:
        arr.remove(min(arr))
        return arr

