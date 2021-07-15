def square_digits(num):
    # s converts num to a str so we can index through it
    # when then loop through the len of the str 
    # while we're looping the string we convert it back to a int and square it
    # after we add it to a str to keep it from adding and then convert it to a int
    s = str(num)
    t = len(s)
    y=0
    g= 0
    b=""
    while y < t:
        g = int(s[y])**2 
        b= b+ str(g) 
        final = int(b)
        y=y+1
    return(final)   
    pass
