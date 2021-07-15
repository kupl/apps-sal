def power_of_two(x):
    powers = []
    for i in range(0,5000):
        powers.append(2**i)
    if x in powers:
        return True
    else:
        return False

