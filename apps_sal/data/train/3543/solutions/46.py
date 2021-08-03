import re


def increment_string(strng):
    return '1' if len(strng) == 0 else strng[:-1] + str(int(strng[len(strng) - 1]) + 1) if strng[len(strng) - 1].isdigit() and 0 <= int(strng[len(strng) - 1]) <= 8 else strng + '1' if not strng[len(strng) - 1].isdigit() else strng[:-len((re.search(r'\d9+$', strng))[0])] + str(int((re.search(r'\d9+$', strng))[0]) + 1)
