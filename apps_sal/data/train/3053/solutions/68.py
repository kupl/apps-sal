def close_compare(a, b, margin=0):
    return 0 if a in range(b - margin, b + margin + 1) else -1 if a < b else 1
