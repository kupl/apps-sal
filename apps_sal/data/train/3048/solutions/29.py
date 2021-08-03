def alternateCase(s):

    result = ""
    for char in s:
        ascii_value = ord(char)
        if (97 <= ascii_value <= 122):
            ascii_value -= 32
        elif (65 <= ascii_value <= 90):
            ascii_value += 32

        result += chr(ascii_value)

    return result
