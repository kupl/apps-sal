def string_clean(s):
    no_digits = []
    for i in s:
        if not i.isdigit():
            no_digits.append(i)
    result = ''.join(no_digits)
    return result
