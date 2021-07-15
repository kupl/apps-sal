def is_palindrome(string):
    if type(string) == int: string = str(string)
    if len(string) < 2: return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])
