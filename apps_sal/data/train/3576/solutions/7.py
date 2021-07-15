def longest(words):
    biggest = 0
    for word in words:
        if len(word) > biggest:
            biggest = len(word)
    return biggest 
