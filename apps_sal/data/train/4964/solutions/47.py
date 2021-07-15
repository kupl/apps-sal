def is_uppercase(inp):
    return False if any([x.islower() for x in inp]) else True
