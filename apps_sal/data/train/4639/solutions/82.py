def power_of_two(x):
    powers = []
    for i in range(0, 1000):
        powers.append(2 ** i)
    return True if x in powers else False
