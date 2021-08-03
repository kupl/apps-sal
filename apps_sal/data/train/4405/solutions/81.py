def is_palindrome(string):

    s = str(string)
    l = len(s)
    l2 = l // 2

    if l % 2 == 0 and s[0:l2] == s[l2::][::-1]:
        return True
    elif l % 2 == 0 and s[0:l2] != s[l2::][::-1]:
        return False
    elif l % 2 != 0 and s[0:l2] == s[l2 + 1::][::-1]:
        return True
    elif l % 2 != 0 and s[0:l2] != s[l2 + 1::][::-1]:
        return False
    else:
        return None
