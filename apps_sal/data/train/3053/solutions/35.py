def close_compare(a, b, margin=0):
    prox = a - b
    if abs(prox) <= margin:
        return 0
    elif a > b:
        return 1
    else:
        return -1
