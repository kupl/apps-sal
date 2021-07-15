def solve(arr):
    return [sum(ord(v) - 96 == i for i,v in enumerate(word.lower(), 1)) for word in arr]
