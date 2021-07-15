def tidyNumber(n):
    a = str(n)
    index = 0
    while index<len(a)-1:
        if int(a[index])>int(a[index+1]):
            return False
        index +=1
    return True
