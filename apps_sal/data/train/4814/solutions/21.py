def is_palindrome(s):
    output = True
    s = s.upper()
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            output = False
    return output
