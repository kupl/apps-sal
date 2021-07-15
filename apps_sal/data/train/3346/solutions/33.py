def gap(g, m, n):
    
    def is_prime(p):
        if p % 2 == 0: return False
        for i in range(3, int(p**0.5)+1, 2):
            if p % i == 0: return False
        return True

    first = 0
    for t in range(m, n+1):
        #print(t, first)
        if not(is_prime(t)): continue
        #print(t, 'is prime')
        if first == 0:
            first = t
            #print(first, 'is first')
        elif t - first == g:
            return [first, t]
        else:
            first = t
    
#    prime_list = []        
#    for t in range(m, n+1):
#        if is_prime(t): prime_list.append(t)
#    
#    for i in range(len(prime_list) - 1):
#        if prime_list[i+1] - prime_list[i] == g:
#            return [prime_list[i], prime_list[i+1]]
    
    return None
