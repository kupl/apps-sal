def is_palindrome(string):
    print(string)
    return str(string) == ''.join(list(reversed(str(string))))
