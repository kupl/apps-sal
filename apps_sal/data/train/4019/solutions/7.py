def max_multiple(divisor, bound):
    #your code here
    while bound > divisor:
        if bound % divisor == 0:
            return bound
        else:
            bound = bound - 1
            return max_multiple(divisor, bound)
