def to_freud(sentence):
    ctr = 0
    try:
        cunt = sentence.split()
        for fuck in cunt:
            cunt[ctr] = "sex"
            ctr += 1
        return ' '.join(cunt)
    except:
        "(empty string)"
