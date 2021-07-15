def palindrome(num):
    if (isinstance(num, int)== False) or (num < 0):
        return 'Not valid'
    else:
        if str(num) == str(num)[::-1]:
            return True
        else:
            return False
