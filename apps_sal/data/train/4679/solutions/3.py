def to_freud(sentence):
    words = sentence.split()
    wordcount = len(words)
    s = ""
    while wordcount > 0:
        s = s + "sex "
        wordcount -= 1
    return s[:-1]
