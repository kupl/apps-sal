def remove_duplicate_words(s):
    seperated = s.split()
    mylist = list( dict.fromkeys(seperated))
    return ' '.join(mylist)
