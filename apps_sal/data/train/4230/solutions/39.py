def reverse_letter(string):
    word = []
    for i in string:
        if i.isalpha() == True:
            word.append(i)
    word = reversed(word)
    word_rev = ''.join(word)
    return word_rev
