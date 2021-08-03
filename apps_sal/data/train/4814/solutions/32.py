def is_palindrome(s):

    if(len(s) == 0):
        return True
    if len(s) == 1:
        return True
    if len(s) == 2:
        if str(s[0]).lower() == str(s[1]).lower():
            return True
    if s[0] != '' and s[-1] != '':
        if str(s[0]).lower() == str(s[-1]).lower():
            return is_palindrome(s[1:len(s) - 1])

    return False
