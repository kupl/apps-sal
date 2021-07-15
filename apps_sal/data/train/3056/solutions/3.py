def palindrome(num,s):
    if type(num)!=int or type(s)!=int or num<0 or s<0:
        return 'Not valid'
    res=[]
    i=max(11,num)
    while len(res)<s:
        if str(i)==str(i)[::-1]:
            res.append(i)
        i+=1
    return res
