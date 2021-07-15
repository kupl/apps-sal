def tidyNumber(n):
    n= str(n)
    back = n[0]
    for number in n:
        if number < back:
           return False
        back = number
    return True
