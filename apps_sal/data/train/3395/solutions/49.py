# Non-regex solution

def remove_duplicate_words(sentence):
    lst = [sentence][0].split()  # split sentence by words and turn into list

    no_dbls = list(dict.fromkeys(lst))  # remove doubles from list

    return (' '.join(no_dbls))  # turn list back to sentence
