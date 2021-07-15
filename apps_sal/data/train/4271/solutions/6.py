dictio = {1:".",2:":",3:":.",4:"::",5:":.:"}
def roman_fractions(integer, fraction=None):
    if integer < 0  or integer > 5000 or fraction and (fraction<0 or fraction>11):
        return "NaR"
    if integer == 0 and not fraction : return "N"
    return encoder(integer) + dictio.get(fraction,"S"+dictio.get(fraction-6,"")) if fraction else encoder(integer)
    
def encoder(n):
    num = "M CM D CD C XC L XL X IX V IV I".split()
    ls = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    s = ""
    for i,j in enumerate(num):
        while n >= ls[i]:
            s += j
            n -= ls[i]
    return s  
