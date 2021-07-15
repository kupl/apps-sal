def is_palindrome(string):
    if type(string)==str:
        return bool(string==string[::-1])
    elif type(string)==int:
        string=str(string)
        return bool(string==string[::-1])
        
    

