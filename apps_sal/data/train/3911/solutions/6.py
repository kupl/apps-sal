def howmuch(m, n):
    parameters = [m, n]
    parameters.sort()
    trueInstances = []
    for instance in range(parameters[0], parameters[1] + 1):
        if (instance - 1) % 9 == 0 and (instance - 2) % 7 == 0:
            carPrice = int((instance - 1) / 9)
            boatPrice = int((instance - 2) / 7)
            statement = [f"M: {instance}", f"B: {boatPrice}", f"C: {carPrice}"]
            trueInstances.append(statement)
    return trueInstances
    # your code
