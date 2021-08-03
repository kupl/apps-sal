def remove_duplicate_words(s):
    s_list = s.split()
    result_list = []

    for word in s_list:
        if word not in result_list:
            result_list.append(word)

    return " ".join(result_list)
