def find_multiples(integer, limit):
    multiplies = []
    for i in range(integer, limit + 1, integer):
        multiplies.append(i)
    return multiplies
