def is_palindrome(string):
    a = len(str(string))
    for i in range(0, a):
        if str(string)[i] != str(string)[a - i - 1]:
            return False
    
    return True
