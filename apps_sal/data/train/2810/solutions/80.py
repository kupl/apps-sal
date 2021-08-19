def solve(arr):
    return [sum((1 for (i, c) in enumerate(strng.lower()) if i == ord(c) - 97)) for strng in arr]
