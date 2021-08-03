def is_inertial(a):
    odd = {i for i in a if i % 2}
    even = set(a) - odd
    if not even:
        return False
    q = sorted(even)[-2] if len(even) > 1 else sorted(even)[0]
    return odd and max(even) > max(odd) and min(odd) > q
