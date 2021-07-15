def tidyNumber(n):
    n = str(n)
    backnumber = n[0]
    for number in n:
        if number < backnumber:
           return False
        backnumber = number
    return True
