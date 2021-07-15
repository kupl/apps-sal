def solve(arr):
    return [sum(1 for i,c in enumerate(w) if i == 'abcdefghijklmnopqrstuvwxyz'.index(c.lower()) ) for w in arr]
