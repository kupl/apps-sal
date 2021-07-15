def swap(string_):
    return string_.translate(str.maketrans('aeiou', 'AEIOU'))
