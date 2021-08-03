def remove_duplicate_words(s):
    d = s.split()
    d = list(dict.fromkeys(d))
    print(d)
    anwser = " ".join(d)
    return anwser
