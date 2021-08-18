def first_non_repeating_letter(some_string):
    return ''.join([char if some_string.lower().count(char.lower()) == 1 else '' for char in some_string])[:1]
