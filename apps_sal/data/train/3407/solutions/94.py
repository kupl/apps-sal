def palindrome_chain_length(n, s=0):
    if str(n) == str(n)[::-1]:
        return s
    else:
        return palindrome_chain_length(n + int(str(n)[::-1]), s + 1)
