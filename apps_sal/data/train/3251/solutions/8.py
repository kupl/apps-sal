def primeFactors(n):
    ret = ''
    for i in range(2, int(n **0.5)+1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += f'({i}**{num})' if num > 1 else f'({i})'
        if n == 1:
            return ret
        
    return ret + f'({int(n)})'
