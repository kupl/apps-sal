def solve(arr):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return [sum([1 if i == alpha.find(c.lower()) else 0 for i,c in enumerate(x)]) for x in arr]
