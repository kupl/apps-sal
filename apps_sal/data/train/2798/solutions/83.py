def to_alternating_case(string):
    res = ''
    for char in string:
        if char.isalpha():
            res += char.upper() if not char.isupper() else char.lower()
        else:
            res += char
    return res
