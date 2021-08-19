def sum_array(arr):
    if len(arr or []) <= 2:
        return 0
    odd = len(arr) % 2
    if odd:
        total = lowest = highest = arr[0]
    else:
        (total, lowest, highest) = (0, float('inf'), -float('inf'))
    for (a, b) in zip(arr[odd::2], arr[1 + odd::2]):
        total += a + b
        if a > b:
            lowest = min(b, lowest)
            highest = max(a, highest)
        else:
            lowest = min(a, lowest)
            highest = max(b, highest)
    return total - lowest - highest
