def is_uppercase(inp):
    inp = list(map(str, inp.split()))
    for element in inp:
        if not(element.isupper()):
            return False
    return True
