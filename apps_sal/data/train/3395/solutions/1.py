def remove_duplicate_words(s):
    s = s.split(" ")
    words = []
    for item in s:
        if item not in words:
            words.append(item)
    return " ".join(words)

