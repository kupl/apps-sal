def is_palindrome(s):
    reversedstring = ''.join(reversed(s))
    if s.lower() == reversedstring.lower():
        return True
    else:
        return False
