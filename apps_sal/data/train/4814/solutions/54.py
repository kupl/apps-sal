def is_palindrome(s):
    dni = 0
    ri = True
    for x in s:
        dni -= 1
        if x.lower() == s[dni].lower():
           ri = True
        else:
            ri = False
            break
    return ri


