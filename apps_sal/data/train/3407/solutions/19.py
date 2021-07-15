def palindrome_chain_length(n):
    return 0 if int(str(n)[::-1]) == n else palindrome_chain_length(int(str(n)[::-1]) + n) + 1

