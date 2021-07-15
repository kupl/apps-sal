def capitalize(s):
    a = "".join([char.upper() if not index%2 else char for index, char in enumerate(s)])
    b = "".join([char.upper() if index%2 else char for index, char in enumerate(s)])
    return [a, b]
