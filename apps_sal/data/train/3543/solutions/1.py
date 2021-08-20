def increment_string(strng):
    stripped = strng.rstrip('1234567890')
    ints = strng[len(stripped):]
    if len(ints) == 0:
        return strng + '1'
    else:
        length = len(ints)
        new_ints = 1 + int(ints)
        new_ints = str(new_ints).zfill(length)
        return stripped + new_ints
