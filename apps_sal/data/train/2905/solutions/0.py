def nickname_generator(name):
    return "Error: Name too short" if len(name) < 4 else name[:3+(name[2] in "aeiuo")]
