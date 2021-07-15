def solve(arr): 
    ls = []
    for x in arr[::-1]:
        if ls.count(x) == 0:
            ls.append(x)
    return [i for i in ls[::-1]]
