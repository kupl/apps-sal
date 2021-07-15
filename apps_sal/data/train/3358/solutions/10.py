def correct(string):
    return string.translate(bytes.maketrans(b"501",b"SOI"))
