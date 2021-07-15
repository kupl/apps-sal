def lovefunc( flower1, flower2 ):
    x = flower1 % 2 == 0 and flower2 % 2 == 1
    y = flower2 % 2 == 0 and flower1 % 2 == 1
    return True if x or y else False
