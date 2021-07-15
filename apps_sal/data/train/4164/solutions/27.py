def first_non_repeating_letter(string):
    is_unique = lambda char: string.lower().count(char.lower()) == 1
    return next((char for char in string if is_unique(char)), '')
