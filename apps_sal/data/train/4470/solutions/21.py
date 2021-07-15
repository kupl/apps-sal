def nb_year(p0, percent, aug, p):
    n = p0 + p0* (percent/100) + aug
    nb= 1 
    while n < p:
        n = n + n*(percent/100) + aug
        nb += 1
    return(nb)
        





