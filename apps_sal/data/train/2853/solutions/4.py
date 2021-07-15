def solve(arr): 
    seen = set()
    return [seen.add(a) or a for a in reversed(arr) if a not in seen][::-1]
