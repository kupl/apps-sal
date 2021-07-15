def to_freud(sentence):
    l = len(sentence.split(" "))
    return ' '.join(["sex" for _ in range(l)])
