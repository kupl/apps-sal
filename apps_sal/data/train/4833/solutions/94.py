def replace_exclamation(s):
    new = ''
    for x in s:
        if x in "aeiouAEIOU":
            new += '!'
        else:
            new += x
    return new
