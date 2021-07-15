def no_space(x):
    res = ""
    for char in x:
        if char != " ":
            res += char
    return res
