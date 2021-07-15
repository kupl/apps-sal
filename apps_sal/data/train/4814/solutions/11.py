def is_palindrome(s):
    for i in range(len(s)):
        if s[i].upper() != s[len(s) - 1 -i].upper():
            return False
    return True

