def reverseWords(r):
    s=r.split()
    r=''
    for i in range(1,len(s)+1):
        r+=s[-i]+' '
    return r[:-1]
