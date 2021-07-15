def capitalize_word(word):
    word_2 = ""
    for i in range(len(word)):
        if i == 0:
            word_2 += word[i].upper()
        else:
            word_2 += word[i]
    return word_2
