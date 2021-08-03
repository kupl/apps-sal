def palindrome_chain_length(n):
    n = str(n)
    if(n == n[::-1]):
        return 0
    return 1 + palindrome_chain_length(int(n) + int(n[::-1]))
