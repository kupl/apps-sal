def calculate_probability(n):
    
    year = 365
    numer = 1
    den = 365 ** n
    
    while n > 0:
        print(year)
        numer *= year
        n -= 1
        year -= 1
    
    return round((1 - (numer/den)) , 2)
