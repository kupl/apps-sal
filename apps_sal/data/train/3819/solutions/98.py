def smash(words):
    sentence = ""
    length_words = len(words)
    for word in words:
        sentence += word
        if word == words[-1]:
            pass
        else:
            sentence += ' '
    return(sentence)

