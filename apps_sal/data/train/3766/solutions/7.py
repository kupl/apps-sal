def getAllPrimeFactors(n):
    if not type(n) is int:
        n = 0
    elif n < 0:
        n = 0
    results = []
    number = 2
    while number < n:
        if not n % number:
            n /= number
            results.append(number)
            number = 2
        else:
            number += 1
    if n: results.append(int(n))
    return results

def getUniquePrimeFactorsWithCount(n):
    results = getAllPrimeFactors(n)
    counted = [[],[]]
    if not results == []:
        for i in range(results[-1]+1):
            if i in results: 
                counted[0].append(i)
                counted[1].append(results.count(i))            
    return counted

def getUniquePrimeFactorsWithProducts(n):
    counted = getUniquePrimeFactorsWithCount(n)
    products = []
    if not counted == [[],[]]:
        for i in range(len(counted[0])):
            products.append(counted[0][i]**counted[1][i])
    return products
