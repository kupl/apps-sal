def is_palindrome(string):
    yazi = str(string)

    if yazi == yazi[::-1]:
        return True
    return False
