def lovefunc(flower1, flower2):
    odd = False
    even = False

    if flower1 % 2 == 0:
        even = True
    elif flower1 % 2 != 0:
        odd = True

    if flower2 % 2 == 0:
        even = True
    elif flower2 % 2 != 0:
        odd = True

    if odd is True and even is True:
        return True
    return False
