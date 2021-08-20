def to_alternating_case(string):
    altstring = ''
    for i in range(len(string)):
        if string[i] == string[i].lower():
            altstring += string[i].upper()
        else:
            altstring += string[i].lower()
    return altstring
