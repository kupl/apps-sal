def to_freud(sentence):
    word=sentence.split()
    a=len(word)
    print(a)
    s=""
    while a > 0:
        s=s+"sex "
        a-=1
    return s[:-1]
    

    

