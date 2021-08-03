def you_are_a_cube(cube):
    if(round(cube ** (1 / 3), 10) == int(round(cube ** (1 / 3), 10))):
        return True
    else:
        return False
