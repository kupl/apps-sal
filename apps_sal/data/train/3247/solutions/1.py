def sort_by_height(arr):
    heights = iter(sorted(i for i in arr if i > 0))
    for idx, i in enumerate(arr):
        if i > 0:
            arr[idx] = next(heights)
    return arr
