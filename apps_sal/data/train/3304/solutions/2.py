def is_inertial(arr):
    (even, odd) = ([], [])
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(odd) == 0 or max(even) != max(arr) or min(odd) < sorted(even)[-2]:
        return False
    else:
        return True
