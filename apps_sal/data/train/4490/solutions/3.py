def max_collatz_length(limit):
    if type(limit) != int or limit < 1:
        return []
    
    results = {1: 1}
    
    for n in range(2, limit + 1):
        count = 0
        x = n
        while x not in results:
            x = x * 3 + 1 if x % 2 else x // 2
            count += 1
        
        count += results[x]
        results[n] = count
    
    sol = max(results, key=results.get)
    return [ sol, results[sol] ]
