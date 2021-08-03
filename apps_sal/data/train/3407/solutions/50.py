def palindrome_chain_length(n):
    rev_n = int((str(n)[::-1]))
    if n == rev_n:
        return 0
    return 1 + palindrome_chain_length(n + int((str(n)[::-1])))
