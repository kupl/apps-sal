def is_palindrome(s):
    a = s.lower()
    b = "".join(reversed(a))
    if a == b:
        return True
    else:
        return False
