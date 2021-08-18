import re


def mouth_size(animal):
    animalnew = animal.lower()
    if animalnew == 'alligator':
        return "small"
    else:
        return "wide"
