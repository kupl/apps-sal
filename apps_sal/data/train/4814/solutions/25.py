def is_palindrome(string):
    return all((s.lower() == e.lower() for (s, e) in zip(string, reversed(string))))
