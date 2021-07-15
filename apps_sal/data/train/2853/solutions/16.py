def solve(a): 
    return list(dict.fromkeys(a[::-1]))[::-1]
