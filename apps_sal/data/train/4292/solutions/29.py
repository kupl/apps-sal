def string_clean(s):

    no_digits = []
    # Iterate through the string, adding non-numbers to the no_digits list
    for i in s:
        if not i.isdigit():
            no_digits.append(i)
    result = ''.join(no_digits)
    return result
