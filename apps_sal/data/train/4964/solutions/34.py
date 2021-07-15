def is_uppercase(inp):
    new_inp = ''
    for char in inp:
        if char == char.upper():
            new_inp += char
    if len(inp) == len(new_inp):
        return True
    else:
        return False
