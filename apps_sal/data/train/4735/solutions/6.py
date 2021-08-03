def keep_order(ar, val):
    for i in range(len(ar)):
        if ar[i] >= val:
            return i
    return len(ar)
