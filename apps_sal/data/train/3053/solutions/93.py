def close_compare(a, b, margin=0):
    return -1 if a + margin < b else int(a - margin > b)
