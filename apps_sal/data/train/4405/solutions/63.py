def is_palindrome(string):
    if type(string)==int:
        n=int(string)
        n1=int(string)
        rev = 0
        while(n > 0): 
            a = n % 10
            rev = rev * 10 + a 
            n = n // 10
        return n1==rev
    else:
        string1=list(string)
        string=list(string)
        string.reverse()
        string2=list(string)
        if string1==string2:
            return True
        return False
