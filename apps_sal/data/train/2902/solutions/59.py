def opposite(number):
    return float("-" + str(number)) if number >= 0 else float(str(number)[1:])
