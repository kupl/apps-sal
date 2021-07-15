def plant_doubling(n):
    powers = [2**i for i in range(30)]
    powers.reverse()
    difference = n
    array = []
    for i in range(30):
        if powers[i] <= difference:
            difference = (difference - powers[i])
            array.append(powers[i])
    return len(array)
