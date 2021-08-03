def string_clean(s):
    return s.translate(s.maketrans({'0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}))
