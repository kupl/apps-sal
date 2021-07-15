def is_palindrome(s):
    s=s.lower()
    n=len(s)
    if n==1:return True
    n=n//2
    for i in range(1,n+1):
        if s[i-1] != s[-i]:
            return False
    return True
