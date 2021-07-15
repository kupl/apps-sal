def solve(arr):
    seen = []
    for i in arr:
        if i in seen:
            seen.remove(i)
            seen.append(i)
        else:
            seen.append(i)
            
    return seen
