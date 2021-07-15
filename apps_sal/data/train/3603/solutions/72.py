def lovefunc( flower1, flower2 ):
    if (flower1 + flower2) % 2 != 0:
        return True
    elif (flower1 + flower2) % 2 == 0 or flower1 + flower2 == 0:
        return False
