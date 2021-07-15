def halving_sum(n): 
    output = 0
    while n > 0:
        output += n
        n //= 2
    return output
