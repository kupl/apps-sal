def is_palindrome(s):
    s=s.lower()
    s1="".join(reversed(s))
    if(s==s1):
        return True
    else:
        return False
