def is_palindrome(string):
    return [*str(string)] == list(reversed([*str(string)]))
