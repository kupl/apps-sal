from collections import Counter

def getAllPrimeFactors(n):
    if n==1: return [1]
    lst, p, n = [], 2, 1 if not isinstance(n,int) or n<0 else n
    while n>1:
        while not n%p:
            lst.append(p)
            n //= p
        p += 1 + (p!=2)
    return lst

def getUniquePrimeFactorsWithCount(n):
    return list(map(list, zip(*Counter(getAllPrimeFactors(n)).items()))) or [[],[]]

def getUniquePrimeFactorsWithProducts(n):
    return [k**v for k,v in Counter(getAllPrimeFactors(n)).items()]
