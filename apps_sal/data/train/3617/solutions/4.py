def is_zero_balanced(arr):
    pos = (n for n in arr if n > 0)
    neg = (-n for n in arr if n < 0)
    return sorted(pos) == sorted(neg) if arr else False
