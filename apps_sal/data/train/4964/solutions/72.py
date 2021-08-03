def is_uppercase(inp):
    return True if len(list(filter(lambda char: char.islower(), inp))) == 0 else False
