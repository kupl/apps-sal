def remove_duplicate_words(s):
    q = ""
    a = s.split(" ")
    for i in a:
        if i not in q:
            q += i + " "
    return q[:-1]
