def fit_in(a,b,m,n):
    if a+b > max(m,n) or a > min(m,n) or b > min(m,n):
        return False
    return a**2 + b**2 <= m*n
