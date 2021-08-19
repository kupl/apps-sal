def nth_smallest(arr, pos):
    for number in arr:
        if pos == 1:
            return min(arr)
        elif pos > 1:
            for to_delete in range(1, pos):
                arr.remove(min(arr))
            return min(arr)
