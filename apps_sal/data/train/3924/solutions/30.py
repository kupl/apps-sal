def reverse_words(text):
    return " ".join(["".join(reversed(list(i))) for i in text.split(" ")])
