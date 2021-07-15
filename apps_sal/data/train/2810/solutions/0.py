def solve(arr):
    return [ sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr ]
