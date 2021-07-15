def close_compare(a, b, margin=0):
    print(a, b, margin)
    if margin == 0:
        return -1 if a < b else 1 if a != b else 0
    else:
        if a == b or abs(a-b) == margin:
            return 0
        elif a < b:
            return 0 if abs(a-b) <= margin else -1
        elif a > b:
            return 0 if abs(a-b) <= margin else 1
