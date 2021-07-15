def capitalize_word(word):
    capLetter = "".join(char.capitalize() for char in word[0])
    capOthers = "".join(char.lower() for char in word[1:10])
    capWord = capLetter + capOthers
    return(str(capWord))
