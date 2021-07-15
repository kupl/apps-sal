def correct(strng):
    return strng.translate(strng.maketrans("501","SOI"))
