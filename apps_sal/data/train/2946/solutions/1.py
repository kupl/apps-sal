def reverse_sentence(sentence):
    return " ".join(word[::-1] for word in sentence.split())
