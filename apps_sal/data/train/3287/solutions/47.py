import re


def mouth_size(animal):

    pattern = re.match(r'alligator', animal, re.I)
    if pattern:
        return "small"
    return "wide"
