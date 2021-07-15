def is_palindrome(string):
    return str(string)==str(string)[::-1] if str(string).isdigit() else string.lower()==string.lower()[::-1]
