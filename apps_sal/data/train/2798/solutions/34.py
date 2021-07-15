def to_alternating_case(string):
    result = ""
    for char in string:
        if char.islower() == True:
            result += char.upper()
        else:
            result += char.lower()
    return result
