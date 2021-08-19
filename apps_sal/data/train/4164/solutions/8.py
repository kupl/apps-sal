def first_non_repeating_letter(string):
    for char in string:
        if string.lower().count(char.lower()) < 2:
            return char
    return ''
