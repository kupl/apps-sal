def is_uppercase(inp):
    return all((i.isupper() for i in ''.join(inp).split()))
