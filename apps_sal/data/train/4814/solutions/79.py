def is_palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start].lower() == s[end].lower():
            start += 1
            end -= 1
        else:
            return False
    return True
