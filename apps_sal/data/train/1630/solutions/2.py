def gcd(a, b):  # Just a simple Euclidean algorithm to compute gcd
    while (b != 0):
        a, b = b, a % b
    return a


def survivor(zombies):

    if (len(zombies) == 0):  # First let's deal with lists of length == 0
        return -1

    zombies.sort()  # Then let's sort the list
    if zombies[0] == 1:  # If zombie[0] is 1, we know every number will be biten
        return 0

    ####################################################################
    #Let's check if there is an infinity of solutions.                 #
    #It is equivalent to see if gcd of all numbers is different from 1.#
    ####################################################################

    zombies_gcd = 0
    for z in zombies:
        zombies_gcd = gcd(z, zombies_gcd)
    if zombies_gcd != 1:
        return -1

    ####################################################################
    #Now let's list every number to see who's the last one to be bitten#
    ####################################################################

    length = zombies[-1] + 1
    who_is_bitten = [False for i in range(length)]

    for z in zombies:  # Of courses zombies are considered as bitten
        who_is_bitten[z] = True

    i = zombies[0] - 1  # We know that zombies[0]-1 is a survivor so we can begin by that number

    # We keep track of the number of consecutive zombies
    consecutive_zombies = 0

    while (consecutive_zombies < zombies[0]):  # we know if there are zombies[0] consecutive zombies in a row,
        # then there won't be any survivor after that
        if not(who_is_bitten[i]):  # If the number is not bitten, then it becomes the new last survivor
            result = i
            consecutive_zombies = 0
        else:  # Otherwise, it bites other numbers which are at range
            consecutive_zombies += 1
            while (i + zombies[-1] >= len(who_is_bitten)):  # if the list is too short we have to add new numbers
                who_is_bitten.append(False)

            for z in zombies:
                who_is_bitten[i + z] = True  # Then number i bites numbers that are at its range

        i += 1

    return result
