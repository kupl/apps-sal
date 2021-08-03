def palindrome_chain_length(n, step=0):
    return step if str(n) == str(n)[::-1] else palindrome_chain_length(n + int(str(n)[::-1]), step + 1)
