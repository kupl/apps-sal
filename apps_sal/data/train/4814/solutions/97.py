def is_palindrome(s):
    palindrome = False
    if len(s) <= 1:
        palindrome = True
    else:
        for i in range(len(s) // 2):
            if s[i].lower() == s[-i - 1].lower():
                palindrome = True
            else:
                palindrome = False
                break
    return palindrome
