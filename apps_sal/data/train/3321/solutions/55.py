def evil(n):
    n=bin(n)
    s=str(n)
    c1=0
    for i in s:
        if(i=='1'):
            c1+=1
    if(c1%2==0):
        return("It's Evil!")
    else:
        return("It's Odious!")

