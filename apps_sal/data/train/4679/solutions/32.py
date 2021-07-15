def to_freud(sentence):
    sex = []
    split = sentence.split()
    for i in split:
        sex.append("sex")
    return  ' '.join(sex)

