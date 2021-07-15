def calculator(a,b,c):
    if type(a) != int or type(b) != int:
        return('unknown value')
    elif c == '+':
        return(int(a)+int(b))
    elif c == '-':
        return(int(a)-int(b))
    elif c == '*':
        return(int(a)*int(b))
    elif c == '/':
        return(int(a)/int(b))
    else:
        return('unknown value')
    pass
