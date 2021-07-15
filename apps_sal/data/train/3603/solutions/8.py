def lovefunc( flower1, flower2 ):
    if (flower1 % 2 == 0 and flower2 % 2) or (flower1 % 2 and flower2 % 2 == 0):
        return True
    else:
        return False
