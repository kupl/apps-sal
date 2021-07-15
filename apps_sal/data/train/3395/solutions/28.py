def remove_duplicate_words(s):
    my_set = []
    for word in s.split(" "):
        try:
            my_set.index(word)
        except ValueError:
            my_set.append(word)
    return " ".join(my_set)
