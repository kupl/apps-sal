def reverse(s):
    return s[::-1]


def is_palindrome(s):
    s = str(s)
    rev = reverse(s)
    if (s == rev):
        return True
    return False
