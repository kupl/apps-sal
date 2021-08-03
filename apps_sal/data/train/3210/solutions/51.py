def get_strings(city):

    string = city.lower().replace(' ', '')
    output = ""
    for char in string:
        if char not in output:
            print((string.count(char)))
            output += (f'{char}:{"*" * string.count(char)},')

    return output[:-1]
