def is_palindrome(string):
    a = []
    for i in str(string):
        a.insert(0, i)
    if list(str(string)) != a:
        return False
    else:
        return True

