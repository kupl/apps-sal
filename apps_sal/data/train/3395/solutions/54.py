def remove_duplicate_words(s):
    words = s.split()
    new_list = []
    for i in words:
        if i not in new_list:
            new_list.append(i)
    new_list = " ".join(new_list)
    return new_list
