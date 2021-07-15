def solve(arr): 
    uniques = set(arr)
    output = []
    for n in arr[::-1]:
        if n in uniques:
            output = [n] + output
            uniques.remove(n)
        if len(uniques) == 0:
            return output
    return output
