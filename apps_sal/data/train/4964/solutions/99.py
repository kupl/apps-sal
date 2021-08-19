def is_uppercase(inp):
    return all((i.isupper() for i in inp if i != ' ' and (not i.isdigit()) and i.isalpha()))
