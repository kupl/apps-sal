def nth_smallest(arr, pos):
    # The quickselect algorithm!
    # O(n) average case and o(n**2) worst case (sorted or reverse sorted list)
    # Using random pivots would better handle edgy edge cases but too lazy for that
    if len(arr) == 1: return arr[0]
    pivot_value = arr[0]
    smaller = [num for num in arr[1:] if num < pivot_value]
    bigger = [num for num in arr[1:] if num > pivot_value]
    count_smaller_or_equal = len(arr) - len(bigger)
    if len(smaller) > pos - 1: # -1 because pos is 1-based
        return nth_smallest(smaller, pos)
    elif count_smaller_or_equal > pos - 1: # -1 because pos is 1-based
        return pivot_value
    else:
        return nth_smallest(bigger, pos - count_smaller_or_equal)
