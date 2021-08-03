import re


def binary_to_string(bits):
    return ''.join(chr(int(byte, 2)) for byte in re.findall(r'\d{8}', bits))
