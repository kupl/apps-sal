def palindrome(n):
    s = str(n)
    return s == s[::-1]

def palindrome_chain_length(n):
    n_chain = 0
    while not palindrome(n):
        n += int(str(n)[::-1])
        n_chain += 1
    return n_chain
