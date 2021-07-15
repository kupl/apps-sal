def spoonerize(words):
    lst = words.split(" ")
    a = list(lst[0]) 
    b = list(lst[1])
    a[0],b[0] = b[0],a[0]
    return "".join(a) + " " + "".join(b)

