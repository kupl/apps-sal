def product(s):
    l= list(s)  
    excl = l.count('!')
    qust = l.count('?')
    if excl == 0 | qust == 0:
        return 0
    else: 
        return (excl*qust)

