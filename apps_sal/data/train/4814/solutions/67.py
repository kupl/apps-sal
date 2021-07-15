def is_palindrome(s):
    s = s.lower()
    return True if s == s[::-1] else False


print(is_palindrome('racasdecar'))
print(is_palindrome('racecaR'))
