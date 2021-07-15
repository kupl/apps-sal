def replace_exclamation(s):
    res =""
    for i in s:
        if i in "aeouiAEOIU":
            res += "!"
        else:
            res += i
    return res
