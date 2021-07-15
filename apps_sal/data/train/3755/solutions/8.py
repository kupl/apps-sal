def KEY(n):
    return n.lower()
def sortme(words):
    words.sort(key=KEY)
    return words
