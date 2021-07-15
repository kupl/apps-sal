def disarium_number(n):
    return [ "Not !!","Disarium !!"][sum(k**(i+1) for i, k in enumerate(map(int, str(n)))) == n]
