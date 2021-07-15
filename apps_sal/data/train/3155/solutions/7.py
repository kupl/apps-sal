def fit_in(a,b,m,n):
    if (min(m, n) >= max(a, b)) and max(m, n) >= a + b: 
        return True
    return False
