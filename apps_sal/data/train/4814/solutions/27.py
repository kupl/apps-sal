def is_palindrome(s):
    return True if s[::-1].casefold()==s.casefold()  else False

