def first_non_repeating_letter(string):
    c = [x for x in string if string.lower().count(x.lower()) == 1]
    if c:
        return c[0]
    else:
        return ''
