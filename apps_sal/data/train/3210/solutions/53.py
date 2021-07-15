def get_strings(str):
    output = ""
    str = str.lower().replace(' ', '')
    for char in str:
        if char not in output:
            output += (f'{char}:{"*" * str.count(char)},');
    return output[:-1]
