def alternateCase(s):
    s_list = s.split()
    new_s = []
    for char in s:
        if char.isupper():
            new_s.append(char.lower())
        else:
            new_s.append(char.upper())

    new_s_string = "".join(new_s)

    return new_s_string
