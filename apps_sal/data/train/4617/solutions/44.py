def powers_of_two(n):
    return  [1] + [2**(x-1) for x in range(2,n+2)]
