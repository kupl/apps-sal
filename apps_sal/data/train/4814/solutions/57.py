def is_palindrome(s):

    l, r = 0, len(s) - 1

    while l < r:
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
