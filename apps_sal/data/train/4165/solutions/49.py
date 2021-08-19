def uni_total(string):
    output = 0
    for letter in string:
        output += ord(letter)
    return output
