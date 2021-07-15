def quadratic(x1, x2):
    ans  = []
    ans.append(1)
    ans.append(-(x1 + x2))
    ans.append(x1*x2)
    return tuple(ans)

