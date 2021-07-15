def deep_count(a):
    total = 0
    for item in a:
        total += 1
        if isinstance(item, list):
            total += deep_count(item)
    return total
