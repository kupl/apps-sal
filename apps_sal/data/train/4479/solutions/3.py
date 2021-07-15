def elements_sum(arr, d = 0):
    lf = len(arr) - 1
    return sum(n[lf - i] if n and len(n) > (lf - i) else d for i,n in enumerate(arr))
