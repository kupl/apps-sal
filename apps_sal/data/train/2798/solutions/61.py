def to_alternating_case(string):
    result = ''
    for i in range(len(string)):
        ascii_code = ord(string[i])
        if 97 <= ascii_code <= 122:
            ascii_code -= 32
        elif 65 <= ascii_code <= 90:
            ascii_code += 32
        result += chr(ascii_code)
    return result
