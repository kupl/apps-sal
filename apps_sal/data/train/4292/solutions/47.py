def string_clean(s):
    return s.translate(str.maketrans({x: "" for x in "1234567890"}))
