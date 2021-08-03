def you_are_a_cube(cube):
    x = round(abs(cube)**(1 / 3))
    if x**3 == cube:
        return True
    else:
        return False
