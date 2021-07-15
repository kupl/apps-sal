def correct_polish_letters(st):

    str = ""

    for x in st:
        if x == "ą":
            str += "a"
        elif x == "ć":
            str += "c"
        elif x == "ę":
            str += "e"
        elif x == "ł":
            str += "l"
        elif x == "ń":
            str += "n"
        elif x == "ó":
            str += "o"
        elif x == "ś":
            str += "s"
        elif x == "ź":
            str += "z"
        elif x == "ż":
            str += "z"
        else:
            str += x
    return (str)
