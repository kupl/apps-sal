def count_find_num(primes, limit):
    base = eval( '*'.join( map(str, primes) ) )
    
    if base > limit:
        return []
    
    results = [base]
    
    for p in primes:
        for num in results:
            num *= p
            while num not in results and num <= limit:
                results += [num]
                num *= p
    
    return [ len(results), max(results) ]
