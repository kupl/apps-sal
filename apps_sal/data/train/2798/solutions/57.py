def to_alternating_case(string):
    output = ''
    for i in string:
        if i == i.lower():
            output += i.upper()
        else:
            output += i.lower()
    return output 
