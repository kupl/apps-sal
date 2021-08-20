def to_alternating_case(string):
    result = ''
    for i in string:
        if i.isupper():
            result += i.lower()
        if i.islower():
            result += i.upper()
        elif i == ' ':
            result += i
        elif i.isalpha() == False:
            result += i
    return result
