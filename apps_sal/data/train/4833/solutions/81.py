def replace_exclamation(s):
    v = "aeiouAEIOU"

    a = ""

    for each in s:
        if each in v:
            a += "!"
        else:
            a += each

    return a
