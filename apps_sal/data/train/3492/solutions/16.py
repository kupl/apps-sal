def correct_polish_letters(st):
    letters = {"ą":"a",
              "ć":"c",
              "ę":"e",
              "ł":"l",
              "ń":"n",
              "ó":"o",
              "ś":"s",
              "ź":"z",
              "ż":"z"}
    result = ""
    for s in st:
        if s in letters:
            result = result + letters.get(s)
        else:
            result = result + s
    return result
