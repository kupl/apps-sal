def reverseWords(s):
    l = s.split(" ")
    v  = []
    for i in l:
        v.insert(0,i)
        v.insert(0," ")
    return "".join(v)[1:]
