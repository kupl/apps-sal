def reverse_words(text):
    # go for it
    # print(text[::-1])
    return " ".join([word[::-1] for word in text.split(" ")])
