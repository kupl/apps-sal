def correct(string):
    return string.translate(string.maketrans("501", "SOI"))
