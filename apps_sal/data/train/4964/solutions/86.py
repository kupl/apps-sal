def is_uppercase(inp):
    return sum([not i.isupper() for i in inp if i.isalpha()]) == 0
