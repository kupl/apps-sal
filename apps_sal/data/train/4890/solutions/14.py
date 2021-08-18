def find_difference(a, b):
    p = 1
    q = 1
    for nums in a:
        p *= nums
    for nums in b:
        q *= nums
    return abs(p - q)
