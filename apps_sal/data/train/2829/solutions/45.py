def array_madness(a, b):
    totalOfA = 0
    totalOfB = 0
    for number in a:
        newNumber = number ** 2
        totalOfA += newNumber
    for number in b:
        newNumber = number ** 3
        totalOfB += newNumber

    if totalOfA > totalOfB:
        return True
    else:
        return False
