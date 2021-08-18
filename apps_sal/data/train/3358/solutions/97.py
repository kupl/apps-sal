def correct(string):

    new_word = []
    for letter in string:
        if letter == "5":
            new_word.append("S")
        elif letter == "0":
            new_word.append("O")
        elif letter == "1":
            new_word.append("I")
        else:
            new_word.append(letter)
    return "".join(new_word)
