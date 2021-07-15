def reverseWords(s):
    l=[]
    l=s.split(" ")
    l.reverse()
    f=""
    for i in l:
        f+=i+" "
    return f[:len(f)-1]
