def to_freud(sentence):
    word = sentence.split()
    wordcount = len(word)
    print(wordcount)
    s = ""
    while wordcount > 0:
        s = s + "sex "
        wordcount -= 1
    return s[:-1]
