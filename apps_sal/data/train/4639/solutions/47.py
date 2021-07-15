def power_of_two(x):
    return x in [2**i for i in range(150) if 2**i<=x]
