def to_alternating_case(string):
    res = []
    for token in string:
        if token.isupper():
            res.append(token.lower())
        elif token.islower():
            res.append(token.upper())
        else:
            res.append(token)
    return "".join(res)
