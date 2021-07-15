def solve(arr):
    return [sum(ord(c.lower()) == i for i, c in enumerate(w, 97)) for w in arr]
