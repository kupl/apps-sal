from re import findall


def string_to_array(s):
    return findall(r'\w+', s) or ['']
