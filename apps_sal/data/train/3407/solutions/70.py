def palindrome_chain_length(n, step=0):
    reversed = int(str(n)[::-1])
    if n == reversed:
        return step
    else:
        return palindrome_chain_length(n + reversed, step + 1)
