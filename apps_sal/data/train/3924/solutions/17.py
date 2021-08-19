def reverse_words(text):
    # go for it
    word = ''
    rev_word = ''
    for i in range(0, len(text)):
        if(text[i] != ' '):
            word = word + text[i]
        else:
            rev_word = rev_word + word[::-1] + text[i]
            word = ''
    return(rev_word + word[::-1])
