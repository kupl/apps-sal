def reverse_by_center(s):
    half = len(s) // 2
    return s[-half:] + s[half:-half] + s[:half]
