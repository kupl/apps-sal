def lovefunc( flower1, flower2 ):
    flower_1 = flower1 / 2
    flower_2 = flower2 / 2
    if flower1 == flower2:
        return False
    elif flower_1 + flower_2 == int(flower_1 + flower_2):
        return False
    else:
        return True
