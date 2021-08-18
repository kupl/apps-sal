def reverse_words(str):
    return " ".join(["".join(word[::-1]) for word in str.split(" ")])
