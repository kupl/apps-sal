def remove_chars(s):
    import string
    return ''.join((c for c in s if c == ' ' or c in string.ascii_letters))
