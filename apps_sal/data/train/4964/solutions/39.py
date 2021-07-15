def is_uppercase(inp):
    for i in inp:
        if i.islower():
            return False
    return True
print(is_uppercase("LD"))
