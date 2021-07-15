def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i].lower() != s[~i].lower():
            return False
    return True

