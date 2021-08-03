s_ = 'abcdefghijklmnopqrstuvwxyz'


def decode(string_):
    if not isinstance(string_, str):
        return "Input is not a string"
    s = ''
    for i in string_:
        if not i.isalpha():
            s += i
        elif i.islower():
            s += s_[-s_.index(i) - 1]
        elif i.isupper():
            s += s_[-s_.index(i.lower()) - 1].upper()
    return s
