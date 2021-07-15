def palindrome_chain_length(n):
  if int(str(n)[::-1]) == n:
    return 0
  else:
    return palindrome_chain_length(n + int(str(n)[::-1])) +1
