def solve(arr): 
    removed = []
    for i in arr[::-1]:
        if not i in removed:
            removed.append(i)
    return removed[::-1]
