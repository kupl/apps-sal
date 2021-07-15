def capitalize(s,ind):
    res = ""
    for key, letter in enumerate(s):
        # if element in list
        if key in ind:
            res += letter.upper()
        else:
            res += letter 
    return res
