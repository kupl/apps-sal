def remove_duplicate_words(s):
    res = ""
    k = s.split()
    for i in k:
        if i not in res:
            res += i + " "

    return res.rstrip()
