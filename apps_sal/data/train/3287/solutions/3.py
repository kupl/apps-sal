import re


def mouth_size(animal):
    return 'small' if re.search('alligator', animal, re.IGNORECASE) else 'wide'
