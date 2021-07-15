def is_palindrome(string):
    x = str(string)
    if x[0] != x[-1]:
        return False
    else:
        if len(x) == 1 or len(x) == 2:
            return True
        else:
            return is_palindrome(x[1:-1])
