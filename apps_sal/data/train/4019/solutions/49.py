def max_multiple(divisor, bound):
    contained = []
    for x in range(divisor, bound + 1):
        if x % divisor == 0:
            contained.append(x)
    return max(contained)
