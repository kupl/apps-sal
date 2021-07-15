def approx_root(n):
    b=int(n**0.5)
    return round(b+(n-b*b)/((b+1)**2-b*b),2)
