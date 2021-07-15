def is_palindrome(str):
    a = str.lower()
    if a == a[::-1]:
        return True
    else:
        return False

