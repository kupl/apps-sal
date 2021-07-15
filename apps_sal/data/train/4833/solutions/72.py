def replace_exclamation(s):
    res = ""
    for i in list(s):
        if i in "aeiouAEIOU":
            res += "!"
        else:
            res += i
    return res
