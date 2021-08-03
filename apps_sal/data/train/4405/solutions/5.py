def is_palindrome(string):
    string = str(string)
    return True if string[:len(string) // 2] in string[len(string) // 2:][::-1] else False
