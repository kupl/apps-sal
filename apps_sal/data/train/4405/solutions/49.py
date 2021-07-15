def is_palindrome(string):
    x = str(string)
    for i in range (0, len(x) - 1):
        if x[i] == x[len(x) - 1 - i]:
            return True
        else:
            return False
    pass
