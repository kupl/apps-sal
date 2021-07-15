def palindrome_chain_length(n):
    return n != int(str(n)[::-1]) and palindrome_chain_length(n + int(str(n)[::-1])) + 1
