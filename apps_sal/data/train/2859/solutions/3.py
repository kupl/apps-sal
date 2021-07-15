def largest_sum(arr):
    current = so_far = 0
    for n in arr:
        current += n
        if current > so_far: so_far = current
        if current <= 0: current = 0
    return so_far
