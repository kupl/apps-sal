def is_palindrome(s):
    if type(s) is str:
        if s == s[::-1]:
            return True
        else:
            return False
    elif type(s) is int:
        if str(s) == str(s)[::-1]:
            return True
        else:
            return False
