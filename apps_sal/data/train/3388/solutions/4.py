import re


def binary_to_string(binary):
    return re.sub('[01]{8}', lambda x: chr(int(x.group(), 2)), binary)
