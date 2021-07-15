def first_non_repeating_letter(string):
    lowercase_str = string.lower()
    for i in string:
        if lowercase_str.count(i.lower()) == 1:
            return i
    return ""
