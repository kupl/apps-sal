def solve(arr):
    a,b,c = sorted(arr)
    s = a+b
    if s < c:
        return s
    else:
        return c + int((s-c)/2)
