def is_palindrome(s):
    return all(s[i].lower() == s[-1 - i].lower() for i in range(len(s)))
