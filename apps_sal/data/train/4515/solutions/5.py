def diff(pairs):
    max_diff = max_pair = 0
    for pair in pairs:
        a, b = pair.split('-')
        current = abs(int(a) - int(b))
        if current > max_diff:
            max_diff = current
            max_pair = pair
    return max_pair
