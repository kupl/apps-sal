from bisect import bisect_left
def productFib(prod, fib=[0,1], prods=[0]):
    while prods[-1] < prod:
        fib.append(fib[-2]+fib[-1])
        prods.append(fib[-2]*fib[-1])
    i = bisect_left(prods, prod)
    return [fib[i], fib[i+1], prods[i]==prod]
