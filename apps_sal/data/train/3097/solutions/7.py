def rad_ladies(name):
    return "".join(char for char in name.upper() if char.isalpha() or char in " !")
