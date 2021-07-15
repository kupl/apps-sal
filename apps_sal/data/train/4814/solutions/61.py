def is_palindrome(s):
    import math
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0].lower() == s[1].lower():
            return True
    for i in range(0, math.floor((len(s) - 1)/2)):
        if s[i].lower() != s[len(s) - 1 - i].lower():
            return False
    return True


