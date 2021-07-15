def palindrome_chain_length(n):
    n1 = int(str(n)[::-1])
    return 0 if n==n1 else 1 + palindrome_chain_length(n+n1)

