def compute_depth(n):
    digits, depth = set(), 0
    while digits < set('0123456789'):
        depth += 1
        digits.update(str(depth * n))
    return depth
