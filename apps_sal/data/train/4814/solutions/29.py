def is_palindrome(s):
    for i in range(len(s)):
        if len(s) <= 1:
            print(s)
            return True
        elif s.lower()[0] != s.lower()[-1]:
            print(s)
            return False
        s = s[1:-1]
    return True    
