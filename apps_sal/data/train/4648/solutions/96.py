def automorphic(n):
    n1 = len(str(n))
    sqr = str(n**2)
    if int(sqr[-n1: len(sqr)])==n:
        return 'Automorphic'
    else:
        return 'Not!!'
        
    # easy way how to slice
    

