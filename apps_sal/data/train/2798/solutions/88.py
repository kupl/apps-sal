def to_alternating_case(string):
    string = [i for i in string]
    for i in range(len(string)):
        if string[i].isupper():
            string[i] = string[i].lower()
        elif string[i].islower():
            string[i] = string[i].upper()
    return ''.join(string)
