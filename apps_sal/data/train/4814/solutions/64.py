def is_palindrome(a):
    s = a.lower()
    if s == s[::-1]:
        return True
    else:
        return False
