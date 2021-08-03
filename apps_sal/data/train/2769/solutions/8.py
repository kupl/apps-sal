import re


def decipher(cipher):
    pattern = re.compile(r'[a-z]')
    num = ''
    code = ''
    for i in cipher:
        num += i
        ascii_char = chr(int(num))

        if pattern.search(ascii_char):
            code += ascii_char
            num = ''

    return code
