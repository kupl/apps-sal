def reverse_sentence(sentence):
    words = sentence.split()
    s = ""
    for w in words:
        s = s + w[::-1] + " "
    return s[:-1]
