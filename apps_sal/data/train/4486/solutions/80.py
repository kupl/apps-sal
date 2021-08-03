def repeat_it(string, n):
    str_ = ''

    if not isinstance(string, str):
        return "Not a string"

    for i in range(n):
        str_ = str_ + string

    return str_
