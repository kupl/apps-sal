def roman_fractions(n, f=0):
    
    if n < 0 or n > 5000 or f < 0 or f > 11: return 'NaR'
    if n + f == 0: return 'N'
    
    s = ''
    for r, d in zip('M CM D CD C XC L XL X IX V IV I'.split(), [1000,900,500,400,100,90,50,40,10,9,5,4,1]):
        appearances = n // d
        s, n = s + r * appearances, n - appearances * d

    return s + ([''] + '. : :. :: :.: S S. S: S:. S:: S:.:'.split())[f]
