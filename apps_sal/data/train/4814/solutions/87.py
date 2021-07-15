def is_palindrome(s):
    b = s.lower()
    if b != b[::-1]:
      return False
    else: 
      return True

