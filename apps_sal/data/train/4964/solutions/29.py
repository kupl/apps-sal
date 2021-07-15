def is_uppercase(inp):
    """Are all the alpha character capital"""
    return True if sum([ord(x) > 96 for x in inp if x.isalpha()]) == 0 else False
