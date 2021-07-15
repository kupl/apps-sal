def is_uppercase(inp):
    return inp.isupper() if any(i.isalpha() for i in inp) else True
