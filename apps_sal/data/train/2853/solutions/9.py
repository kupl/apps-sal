def solve(arr): 
    return list(reversed(list(dict.fromkeys(reversed(arr)))))
