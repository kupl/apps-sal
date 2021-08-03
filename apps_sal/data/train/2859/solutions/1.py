def largest_sum(arr):
    a, b, ar = 0, 0, arr[:]
    for i in ar:
        b += i
        if b < 0:
            b = 0
        if b > a:
            a = b
    return a
