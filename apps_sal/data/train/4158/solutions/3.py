def letter_check(arr):
    a, b = [set(i.lower()) for i in arr]
    return not b - a
