def max_and_min(arr1, arr2):
    (max_diff, min_diff) = (float('-inf'), float('inf'))
    for a in arr1:
        for b in arr2:
            current_sum = abs(b - a)
            max_diff = max(max_diff, current_sum)
            min_diff = min(min_diff, current_sum)
    return [max_diff, min_diff]
