def remove_duplicate_words(string):
    string = string.split(" ")
    lst = []
    for word in string:
        if word not in lst:
            lst.append(word)

    return " ".join(lst)
