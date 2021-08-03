def is_palindrome(s):
    return all(s.lower()[i] == s.lower()[len(s) - 1 - i] for i in range(len(s) // 2))
