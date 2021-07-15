def compress(sentence):
    words = sentence.lower().split()
    uniq = sorted(set(words), key=words.index)
    return "".join(str(uniq.index(word)) for word in words)

