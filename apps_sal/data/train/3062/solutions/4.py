def palindrome(a):
    if type(a) == int:
        if a > 0:
            a = str(a)
            b = a[::-1]
            if a == b:
                return True
            else:
                return False
        else:
            return "Not valid"
    else:
        return "Not valid"
