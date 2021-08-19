def is_palindrome(s):
    # To consider upper and lowercase
    s = s.lower()
    rev = s[::-1]
    # Reversed string using splicing
    if s == rev:
        return True
    else:
        return False
