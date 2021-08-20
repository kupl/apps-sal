def sum_array(arr):
    if not arr or len(arr) == 1:
        return 0
    total = mn = mx = arr[0]
    for x in arr[1:]:
        total += x
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return total - mn - mx
