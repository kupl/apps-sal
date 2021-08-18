def correct_polish_letters(st):
    result = ""
    for letter in st:
        if letter == "ą":
            result += "a"
        elif letter == "ć":
            result += "c"
        elif letter == "ę":
            result += "e"
        elif letter == "ł":
            result += "l"
        elif letter == "ń":
            result += "n"
        elif letter == "ó":
            result += "o"
        elif letter == "ś":
            result += "s"
        elif letter == "ź":
            result += "z"
        elif letter == "ż":
            result += "z"
        else:
            result += letter
    return result

    pass
