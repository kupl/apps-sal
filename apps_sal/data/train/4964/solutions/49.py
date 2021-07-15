def is_uppercase(inp):
    try:
        return inp.isupper()
    except not(inp.isalpha()):
        return True
