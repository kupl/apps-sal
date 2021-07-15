def replace_exclamation(s):
    result = ""
    for char in s:
        if char in "aeiouAEIOU":
            result += '!'
        else:
            result += char
    return result
