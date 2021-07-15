def is_palindrome(string: str) -> bool:
    return str(string) == str(string)[::-1]
