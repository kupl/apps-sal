def solve(arr): 
    return sorted(set(arr), key=lambda n: -arr[::-1].index(n))

