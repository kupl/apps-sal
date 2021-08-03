def is_palindrome(s: str) -> bool:
    return s.lower() == s.lower()[::-1]
