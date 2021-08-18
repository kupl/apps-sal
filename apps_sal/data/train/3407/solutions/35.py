def palindrome_chain_length(n):
    return 0 if str(n)[::-1] == str(n) else 1 + palindrome_chain_length(n + int(str(n)[::-1]))
