def lovefunc(flower1, flower2):
    c = 0
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        c = c + 1
    elif flower2 % 2 == 0 and flower1 % 2 != 0:
        c = c + 1
    else:
        return False
    return c > 0
