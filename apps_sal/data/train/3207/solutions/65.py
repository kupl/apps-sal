def reverseWords(s):
    x=s.split()
    y=x[::-1] 
    strin=''
    for i in y:
        strin+=i+ ' '
    return strin.rstrip()
