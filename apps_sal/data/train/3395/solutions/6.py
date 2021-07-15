def remove_duplicate_words(s):
    new_list = []
    for word in s.split():
        if word not in new_list:
            new_list.append(word)
    return " ".join(new_list)
