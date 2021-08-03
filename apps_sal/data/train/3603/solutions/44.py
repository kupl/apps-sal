def lovefunc(flower1, flower2):
    if (flower1 % 2 == 1 and flower2 % 2 == 0) or (flower2 % 2 == 1 and flower1 % 2 == 0):
        return True
    return False
