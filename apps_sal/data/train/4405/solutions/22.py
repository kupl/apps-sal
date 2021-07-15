def is_palindrome(string):
    try:
        if string == string[::-1]:
            return True
    except:
        if str(string) == str(string)[::-1]:
            return True
    return False
