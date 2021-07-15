def is_uppercase(inp):
    result = []
    for i in inp:
        if i.isalpha() == True and i.isupper() != True:
            return False
        else:
            result.append(True)
    return bool(result)
