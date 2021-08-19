lower = 'abcdefghijklmnopqrstuvwxyz'
table = str.maketrans(lower + lower.upper(), lower[::-1] + lower.upper()[::-1])


def decode(stg):
    if not isinstance(stg, str):
        return 'Input is not a string'
    return stg.translate(table)
