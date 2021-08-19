import re

PATTERN = re.compile("^"
                     "M{0,4}"             # thousands
                     "(CM|CD|D?C{,3})"    # hundreds
                     "(XC|XL|L?X{,3})"    # tens
                     "(IX|IV|V?I{,3})"    # units
                     "$")


def valid_romans(arr):
    return [e for e in arr if e and PATTERN.match(e)]
