def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1) 

def C(n,k):
    if n < k:
        return 0
    return fact(n)//(fact(k)*fact(n-k))

def almost_everywhere_zero(n,k):
    if n == 0 and k > 0:
        return 0
    if k == 0:
        return 1
    ntoString = str(n)
    digits = len(ntoString)
    first_digit = int(ntoString[0]) 
    tight = 0 if len(ntoString) < 2 else int(ntoString[1:])
    # print(n,k,tight,first_digit,digits)
    return (first_digit-1)*(9**(k-1))*C(digits-1,k-1) + almost_everywhere_zero(tight, k-1) + (9**k)*C(digits-1, k)
