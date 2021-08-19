def divide(weight):
    # make sure weight is an even number
    # make sure that each part is at least 2
    return weight % 2 == 0 and weight - 2 >= 2
