def to_freud(sentence):
    words = sentence.split()
    wordcount = len(words)
    print(wordcount)
    s = ""
    while wordcount > 0:
        s = s + "sex "
        wordcount -= 1
    return s[:-1]
    
    

