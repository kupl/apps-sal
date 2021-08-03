def is_uppercase(inp):
    for letter in inp:
        if letter.isupper() == False and letter.isalpha() == True:
            return False
        else:
            continue
    return True
