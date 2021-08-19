def find_short(s):
    l = 100000
    a = s.split(" ")
    for i in a:
        if(len(i) < l):
            l = len(i)
    return l  # l: shortest word length
