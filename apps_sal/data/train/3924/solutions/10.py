def reverse_words(str):
    # go for it
    return " ".join(["".join(word[::-1]) for word in str.split(" ")])
