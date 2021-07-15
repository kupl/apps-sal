def is_palindrome(string):
    if string:
        return str(string) == str(string)[::-1]
    elif string.isalpha():
        return string == string[::-1]
