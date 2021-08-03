def letter_check(arr):
    return set.issubset(*(set(s.lower()) for s in arr[::-1]))
