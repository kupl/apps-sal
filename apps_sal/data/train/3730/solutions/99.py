def capitalize(s):
    first =  "".join(v.upper() if i % 2 == 0 else v for i, v in enumerate(s))
    second =  "".join(v.upper() if i % 2 != 0 else v for i, v in enumerate(s))
    return [first, second]
