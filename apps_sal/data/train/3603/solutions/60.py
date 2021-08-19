def lovefunc(flower1, flower2):
    if flower2 % 2 == 0 and flower1 % 2 == 1:
        return True
    elif flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    else:
        return False
