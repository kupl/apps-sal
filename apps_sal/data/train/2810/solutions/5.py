def solve(arr): 
    return [['abcdefghijklmnopqrstuvwxyz'.index(y) == x  for x,y in enumerate(e.lower())].count(True) for e in arr]

