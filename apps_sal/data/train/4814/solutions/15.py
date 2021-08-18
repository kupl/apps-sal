def is_palindrome(s):

    i = 0
    j = len(s) - 1

    while i < j:
        if ord(s[i]) ^ ord(s[j]) | 32 != 32:
            return False
        i += 1
        j -= 1

    return True
