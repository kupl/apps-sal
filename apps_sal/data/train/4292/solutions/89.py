def string_clean(s):
    new_s = ""
    for letters in s:
        if not 48 <= ord(letters) <= 57:
            new_s += letters
    return new_s
