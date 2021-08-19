def is_palindrome(s):
    return not sum((1 for i in range(len(s)) if s.lower()[i] != s[::-1].lower()[i]))
