def first_non_repeating_letter(string):
    str = string.lower()

    for i, v in enumerate(str):
        if str.index(v) == str.rindex(v):
            return string[i]

    return ""

