def powers_of_two(n):
    if(n == 0):
        return [1]
    return powers_of_two(n-1) + [2**n]
