def is_palindrome(string):
    if type(string) == 'str':
        return string == string[::-1]
    else:
        str1 = str(string)
        return str1 == str1[::-1]
