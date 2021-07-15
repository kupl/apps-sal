def is_digit(n):
    if n.isdigit()==True:
        return (True if int(n)>=0 and int(n)<=9 else False)
    else:
        return False
