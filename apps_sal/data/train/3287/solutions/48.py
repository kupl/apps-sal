import re


def mouth_size(animal):
    if re.search('alligator', animal, re.IGNORECASE):
        return 'small'
    else:
        return 'wide'
