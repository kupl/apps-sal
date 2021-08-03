def lovefunc(flower1, flower2):
    if flower1 % 2 == 0:
        return True if flower2 % 2 > 0 else False
    else:
        return True if flower2 % 2 == 0 else False
