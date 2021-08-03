def first_non_repeating_letter(string):
    return next((x for x in string if string.lower().count(x.lower()) == 1), '')
