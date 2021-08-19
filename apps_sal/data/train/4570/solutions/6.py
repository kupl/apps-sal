import regex


def clean_string(s):
    return regex.sub('[^#]((?R)*)#+|\\A#+', '', s)
