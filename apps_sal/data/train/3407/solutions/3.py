def palindrome_chain_length(n, times=0):
    reversed = int(str(n)[::-1])
    if reversed == n:
        return times
    return palindrome_chain_length(n + reversed, times + 1)
