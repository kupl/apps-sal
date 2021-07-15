def f(n):
    n_ = None
    try:
        n_ = float(n)
    except:
        return(None)
    
    return(n_*(n_+1)/2 if (n_.is_integer() and n_ > 0) else None)
