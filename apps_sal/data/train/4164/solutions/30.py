def first_non_repeating_letter(string):
    return ''.join((i for i in string if string.lower().count(i.lower()) == 1))[:1]
