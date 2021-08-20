def is_uppercase(inp):
    if '@' in inp:
        newstr = inp.replace('@', '')
    return inp.isupper()
