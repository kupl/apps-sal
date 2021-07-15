def isDigit(string):
    a=0
    if string == '':
        return False
    for i in string:
        if i.isalpha():
            a+=1
        elif '-' in string[1:]:
            a+=1
        elif i==' ':
            a+=1
    if a==0:
        return True
    else:
        return False
