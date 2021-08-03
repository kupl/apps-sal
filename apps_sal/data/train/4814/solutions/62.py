def is_palindrome(s):

    for i in range(len(s) // 2):
        if s[i].lower() != s[-i - 1].lower():
            return False
            break
    return True
