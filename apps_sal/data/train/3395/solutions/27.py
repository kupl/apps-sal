def remove_duplicate_words(s):
    result_list = []
    for word in s.split():
        if word not in result_list:
            result_list.append(word)
    return ' '.join(result_list)
