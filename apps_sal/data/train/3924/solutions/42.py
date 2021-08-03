def reverse_words(text):
    new_string = ""
    text = text.split(" ")
    print(text)
    first = True
    for word in text:
        if first == True:
            first = False
        else:
            new_string = new_string + " "
        x = len(word)
        for letter in word:
            new_letter = word[x - 1]
            new_string = new_string + new_letter
            x -= 1
    return new_string
