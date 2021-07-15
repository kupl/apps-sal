def list_squared(m, n):
    result = []
    for number in range(m, n+1):
        s = 0
        
        factors = {1,number}
        for x in range(2, int(number**0.5)+1):
            if number % x == 0:
                factors.add(x)
                factors.add(number/x)
                
        for i in factors:
            s = s + i**2
        if s**0.5 == int(s**0.5):
            result.append([number, s])
    return result
