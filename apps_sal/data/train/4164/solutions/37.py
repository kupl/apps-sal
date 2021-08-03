def first_non_repeating_letter(string):

    if all([string.count(item) > 1 for item in string]):
        return ""
    for i, item in enumerate(string.upper()):
        if string.upper().count(item) == 1:
            return string[i]
