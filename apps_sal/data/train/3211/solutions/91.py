def divide(weight):
    quotient = weight / 2
    remainder = weight % 2
    if remainder == 0 and quotient != 1:
        return True
    else:
        return False
