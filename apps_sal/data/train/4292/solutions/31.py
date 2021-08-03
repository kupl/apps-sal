def string_clean(s):
    new = ""
    for char in s:
        if char.isdigit():
            new += ""
        else:
            new += char

    return new
