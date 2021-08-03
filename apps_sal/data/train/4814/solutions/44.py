def is_palindrome(s):
    x = s.lower()
    if x[::-1] == x:
        return True
    else:
        return False
