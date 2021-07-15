def divisors(n):
    i = 1
    result = 0
    while i <= n:
        if n%i == 0:
            result += 1
        i+=1
    return result
