def remove_duplicate_words(s):
    string = []
    for i in s.split():
        if i not in string:
            string.append(i)
    return ' '.join(string)
