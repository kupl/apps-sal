def first_non_repeating_letter(string):
    return next((ch for ch in string if string.lower().count(ch.lower()) == 1), '')
