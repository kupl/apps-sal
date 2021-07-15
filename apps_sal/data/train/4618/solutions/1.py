def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum
