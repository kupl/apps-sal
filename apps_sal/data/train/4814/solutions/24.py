def is_palindrome(s):
    s=s.lower()
    a=s[::-1]
    if a == s :
        return True
    if a !=s :
        return False
