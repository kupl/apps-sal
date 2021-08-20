def is_uppercase(inp):
    return all((i == True for i in inp.replace(' ', '') if i == i.lower() and i.isalpha()))
