import re


def look_and_say_sequence(data, n):
    return data if n == 1 else look_and_say_sequence(''.join((f'{len(e.group(0))}{e.group(1)}' for e in re.finditer('(\\d)\\1*', data))), n - 1)
