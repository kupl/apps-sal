def is_palindrome(s):
    return False if sum([1 for i in range(len(s)) if s[i].lower() != s[len(s) - 1 - i].lower() ]) else True

