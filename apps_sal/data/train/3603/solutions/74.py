def lovefunc(flower1, flower2):
    f1 = int(flower1)
    f2 = int(flower2)
    if f1 % 2 == 0 and f2 % 2 == 0:
        return False
    elif f1 % 2 != 0 and f2 % 2 != 0:
        return False
    else:
        return True
