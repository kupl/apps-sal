def correct(string):
    #    for i in string:
 #       if i == "5":
    #            string = string.replace("5","S")
 #       if i == "0":
  #          string = string.replace("0","O")
  #      if i == "1":
 #           string = string.replace("1","I")
    # return string

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
