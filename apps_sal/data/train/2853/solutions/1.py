def solve(arr): 
    return list(dict.fromkeys(arr[::-1]))[::-1]
