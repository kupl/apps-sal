def solve(arr):
    return [sum(c.lower() == chr(97+i) for i,c in enumerate(w)) for w in arr]
