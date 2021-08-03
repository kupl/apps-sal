def to_alternating_case(string):

    for char in string:
        '''if char.isupper():
            str_ += char.lower()
        elif char.islower():
            str_ += char.upper()
        elif char == " ":
            str_ += " "
        elif string.isdigit():
            return str(string)
        '''
        a = string.swapcase()

    return a


print(to_alternating_case("cIao"))
