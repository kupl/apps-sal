def is_palindrome(s):
    x = s[::-1].lower()
    if s.lower() == x:
        return True
    else:
        return False
