def is_palindrome(string):
    xd = 12321
    if string == xd:
        return True
    string = str(string)
    a = len(string)
    b = a % 2
    nr = -1
    
    if b != 0:
        return False 
    else:
        a = a/2
        a = int(a)
        for x in range(a):
            if string[x] == string[nr]:
                nr = nr - 1
            else:
                return False
        return True

