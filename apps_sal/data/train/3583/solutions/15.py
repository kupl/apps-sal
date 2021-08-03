import re


def binary_array_to_number(arr):
    binaryString = ''.join(re.findall(r'\d', str(arr)))
    return int(binaryString, 2)
