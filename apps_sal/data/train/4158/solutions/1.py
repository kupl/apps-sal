def letter_check(arr):
    a, b = (set(s.lower()) for s in arr)
    return b <= a
