def isDigit(string):
    # 11ELF
    decnumber = 0

    str = string.strip()
    if len(str) < 1:
        return False

    if "-" == str[0]:
        str = str[1:]

    for character in str:
        if not character.isdigit() and character != ".":
            return False
        if character == ".":
            decnumber = decnumber + 1
        if decnumber > 1:
            return False

    return True
