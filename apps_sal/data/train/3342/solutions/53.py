def pattern(n):
    if n<=0:
        return ""
    
    res="1"
    for i in range(2,n+1):
        add= "\n{}".format(str(i)*int(i))
        res+=add
    return "1" if n==1 else res
