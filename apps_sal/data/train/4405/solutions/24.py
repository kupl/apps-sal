def is_palindrome(string):
    s = str(string)
    if s[::-1] == s:
        return True
    else:
        return False
