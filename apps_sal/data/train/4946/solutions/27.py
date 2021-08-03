def house_numbers_sum(inp):
    suma = 0
    for i in range(len(inp)):
        if inp[i] == 0:
            break
        else:
            suma += inp[i]

    return suma

    # create count variable to count the sum before 0
    # calculate the sum before 0
    # and return the sum
