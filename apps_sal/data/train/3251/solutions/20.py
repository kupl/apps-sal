def primeFactors(n):
    c = 0
    m = 2
    r = []
    while(True):
        if n == 1:
            r.append('(' + str(m) + ')')
            return ''.join(r)
        if n % m == 0:
            n = n / m
            c += 1
        else:
            if c != 0 and c != 1:
                r.append('(' + str(m) + '**' + str(c) + ')')  
            if c == 1:
                r.append('(' + str(m) + ')')
            m += 1
            c = 0
            

