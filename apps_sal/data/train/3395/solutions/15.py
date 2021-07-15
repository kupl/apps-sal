def remove_duplicate_words(s):
    s_list = s.split()
    new_list = []
    for word in s_list:
        if word not in new_list:
            new_list.append(word)
    return ' '.join(new_list)
