def is_uppercase(inp):
    return not len(set(inp).intersection(set('abcdefghijklmnopqrstuvwxyz')))
