def string_clean(s):
    """
    Function will return the cleaned string
    """
    x = []
    for i in range(len(s)):
        if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            x = x
        else:
            x.append(s[i])
    return(''.join(map(str, x)))
