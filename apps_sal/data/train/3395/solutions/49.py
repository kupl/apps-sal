
def remove_duplicate_words(sentence):
    lst = [sentence][0].split()

    no_dbls = list(dict.fromkeys(lst))

    return (' '.join(no_dbls))
