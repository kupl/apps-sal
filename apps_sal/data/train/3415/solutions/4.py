def build_palindrome(s):
  for i in range(len(s)):
      x = s + s[:i][::-1]
      if x == x[::-1]:
          return x
