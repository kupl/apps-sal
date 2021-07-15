def first_non_repeating_letter(string):
    for x in string:
        if string.lower().count(x.lower()) == 1:
            return x
    return ''
