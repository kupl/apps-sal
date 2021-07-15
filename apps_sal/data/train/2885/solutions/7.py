def champernowne_digit(n):
    if not type(n) is int or n < 1:
        return float("NaN")
    n, i, l = n-1, 1, 10
    while n >= l: 
        n, i, l = n-l, i+1, 9 * (i+1) * 10**i
    return (n//(i*10**(i-1-n%i)))%10 + (n%i<1) - (i<2) 

champernowneDigit = champernowne_digit

