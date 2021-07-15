def is_palindrome(string):
    if isinstance(string, int):
        return list(str(string)) == list(str(string)[::-1])
    elif isinstance(string, str):
        return string[::-1] == string
    else:
        pass
