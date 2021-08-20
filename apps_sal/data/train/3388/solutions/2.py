def binary_to_string(binary):
    result = ''
    while binary:
        result += chr(int(binary[:8], 2))
        binary = binary[8:]
    return result
