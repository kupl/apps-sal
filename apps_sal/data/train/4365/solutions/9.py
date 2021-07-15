def is_isogram(string):
    result = {char: string.lower().count(char) for char in string.lower()}
    if 2 in result.values():
        return False
    else:
        return True
