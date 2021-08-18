import re

PATTERN = re.compile("^"
                     "M{0,4}"
                     "(CM|CD|D?C{,3})"
                     "(XC|XL|L?X{,3})"
                     "(IX|IV|V?I{,3})"
                     "$")


def valid_romans(arr):
    return [e for e in arr if e and PATTERN.match(e)]
