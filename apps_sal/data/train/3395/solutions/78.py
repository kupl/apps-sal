from collections import Counter
def remove_duplicate_words(s):
    new=[]
    for i in Counter(s.split(' ')):
        new.append(i)
    return " ".join(new)
