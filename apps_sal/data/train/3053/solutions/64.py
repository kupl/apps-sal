def close_compare(a, b, margin=0):
    if a in range(b - margin, b + margin + 1):
        return 0
    if a > b + margin:
        return 1
    if a < b + margin:
        return -1
