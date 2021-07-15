def palindrome_chain_length(n):
    return 0 if n==int(str(n)[::-1]) else 1 + palindrome_chain_length(n+int(str(n)[::-1]))

