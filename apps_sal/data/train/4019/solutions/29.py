def max_multiple(divisor, bound):
    array = [ i for i in range(1, bound + 1)]
    array.reverse()
    for n in array:
        if n % divisor == 0:
            return n
