def solve(arr):
    return [len([ord(c.lower()) - 97 for (idx, c) in enumerate(a) if ord(c.lower()) - 97 == idx]) for a in arr]
