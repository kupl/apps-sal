def to_freud(sentence):
    i = 0
    for x in sentence.split():
        i += 1
    return (i * "sex ").strip()
