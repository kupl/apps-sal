def hydrate(drink_string): 
    n = sum([int(a) for a in drink_string if a.isnumeric()])
    return str(n) +' glass of water' if n==1 else str(n) +' glasses of water'
    pass
