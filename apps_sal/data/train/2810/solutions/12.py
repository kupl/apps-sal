def solve(arr):
    return [sum((ord(ltr) == i + 65 for (i, ltr) in enumerate(str.upper()))) for str in arr]
