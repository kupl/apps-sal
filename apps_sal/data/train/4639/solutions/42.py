def power_of_two(x):
    list_of_powers = []
    for i in range(500):
        list_of_powers.append(2**i)
    if x in list_of_powers:
        return True
    return False
