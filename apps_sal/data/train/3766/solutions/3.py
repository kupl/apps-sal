
        
def getAllPrimeFactors(n):
    result = []
    if isinstance(n, int) and n > 0 :
        if n == 1:
            result = [1]
        number = 2
        while n > 1:
            print(n)
            if not n % number :
                result.append(number)
                n /= number
                number = 2
            else:
                number += 1
    return result
                
            
  #your code here

def getUniquePrimeFactorsWithCount(n):
    pf = getAllPrimeFactors(n)
    r1 = []
    r2 = []
    if pf:
        r1 = list(set(pf))
        r2 = [pf.count(x) for x in r1 ]
    return [r1, r2]
                

def getUniquePrimeFactorsWithProducts(n):
    return [x ** y for (x,y) in zip(*getUniquePrimeFactorsWithCount(n))]
