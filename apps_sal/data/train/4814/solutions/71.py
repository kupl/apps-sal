def is_palindrome(str):
    s = str.lower()
    if len(s) <= 1:
        return True
    left = 0
    right = len(s) - 1
    if s[left] == s[right] and is_palindrome(s[left + 1:right]):
        return True
    return False
