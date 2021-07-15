def lcm_cardinality(n):
    cardinality = 1
    divisor = 2
    while n>1:
        order = 0
        while n%divisor==0:
            n //= divisor
            order += 1
        cardinality *= 2*order+1
        divisor += 1
    return (cardinality+1)//2

