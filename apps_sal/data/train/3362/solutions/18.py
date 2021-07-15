def sum_mix(arr):
    sum_ = 0
    for item in arr:
        if isinstance(item, (str)):
            sum_ += int(item)
        elif isinstance(item, (int, float)):
            sum_ += item
    return sum_
