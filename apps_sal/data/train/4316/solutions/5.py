def reverse_by_center(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid:] + s[:mid]
    return s[mid+1:] + s[mid] + s[:mid]

