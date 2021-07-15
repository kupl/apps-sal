def to_alternating_case(string):
    new_string = ''
    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string
    #your code here

