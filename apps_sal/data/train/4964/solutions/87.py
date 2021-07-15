def is_uppercase(inp):
    for i in range(len(inp)):
        if inp[i].islower() == True:
            return False
    return True
