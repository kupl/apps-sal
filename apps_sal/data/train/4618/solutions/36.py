def positive_sum(arr):
    total = 0
    for a in arr:
        if "-" not in str(a):
            total += a

    return total
