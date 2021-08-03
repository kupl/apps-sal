def first_non_repeating_letter(string):
    str = string.lower()
    for x in str:
        if str.count(x) == 1:
            return string[str.index(x)]
    return ''
