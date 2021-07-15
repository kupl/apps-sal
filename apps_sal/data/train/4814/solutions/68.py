def is_palindrome(s):
    s=s.lower()
    if len(s) == 1 or len(s)==0:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False
