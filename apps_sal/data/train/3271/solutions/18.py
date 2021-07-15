def arr(n=0): 
    if n == None: return []
    if n == 0: return []
    if n == 1: return [0]
    else: return arr(n-1) + [n-1]
