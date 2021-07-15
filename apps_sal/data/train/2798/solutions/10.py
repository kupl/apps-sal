def to_alternating_case(string):
    string_2 = ''
    for char in string:
        if char.islower():
            string_2 += char.upper()
        else:
            string_2 += char.lower()
    return string_2
