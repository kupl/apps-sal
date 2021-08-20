def is_uppercase(inp):
    return all((i.isupper() for i in inp.replace(' ', '') if i.isalpha()))
