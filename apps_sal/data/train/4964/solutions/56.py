def is_uppercase(inp):
    for i in inp:
        if i.isupper() == False and i.isalpha() == True:
            return False
    return True

