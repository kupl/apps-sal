def max_tri_sum(numbers):
    arr = list(set(numbers))
    a = sorted(arr, reverse=True)
    sum = a[0] + a[1] + a[2]
    return sum
