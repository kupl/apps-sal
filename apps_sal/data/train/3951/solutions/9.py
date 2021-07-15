def duplicate_count(text):
    n=0
    text=text.lower()
    for i in set(text):
        if text.count(i) >1:
            n+=1
    return n
