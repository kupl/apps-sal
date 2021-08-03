def solve(a, b):
    x = sum([1 for i in range(3) if a[i] > b[i]])
    y = sum([1 for i in range(3) if a[i] < b[i]])
    if x > y:
        return f'{x}, {y}: Alice made "Kurt" proud!'
    elif x < y:
        return f'{x}, {y}: Bob made "Jeff" proud!'
    else:
        return f'{x}, {y}: that looks like a "draw"! Rock on!'
