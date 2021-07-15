def remove_duplicate_words(s):
    removed = s.split()
    newlist = []
    for i in removed:
        if(i not in newlist):
            newlist.append(i)
    newstring = " ".join(newlist)
    return newstring
            


