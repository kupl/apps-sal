def first_non_repeating_letter(string):
    print(string)
    for l in string:
        if string.lower().find(l.lower(), string.find(l) + 1) == -1:
            return l
    return ''
