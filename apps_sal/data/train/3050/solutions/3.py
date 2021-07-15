def lcs(x, y):
    if not x or not y: return ""
    if x[0] == y[0]: return x[0] + lcs(x[1:], y[1:])
    
    return max(lcs(x[1:], y), lcs(x, y[1:]), key=len)

