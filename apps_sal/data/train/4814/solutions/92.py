def is_palindrome(s):
    l = len(s)
    if l == 1:
        return True
    for i in range(int(len(s) / 2)):
        if s[i].lower() != s[l - i - 1].lower():
            return False
    return True
