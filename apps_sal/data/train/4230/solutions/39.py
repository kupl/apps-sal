def reverse_letter(string):
    # do your magic here
    word = []
    for i in string:
        if i.isalpha() == True:
            word.append(i)

    word = reversed(word)

    word_rev = "".join(word)

    return word_rev
