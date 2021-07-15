def to_alternating_case(string):
    output = ""
    for str in string:
        if str.isupper():
            output += str.lower()
        elif str.islower():
            output += str.upper()
        elif str == " ":
            output += " "
        else:
            output += str
    return output
