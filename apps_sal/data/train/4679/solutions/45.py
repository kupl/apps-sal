def to_freud(sentence):
    sentence = sentence.split()
    a = ""
    for el in sentence:
        el = "sex"
        a += el + " "
    return a[:-1]
