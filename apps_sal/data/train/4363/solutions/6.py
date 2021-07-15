def reverser(sentence):
    newsent = sentence.split(" ")
    rnsent = [i[::-1] for i in newsent]
    s = " "
    s = s.join(rnsent)
    return s
