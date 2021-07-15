def is_palindrome(n):
    return n == reverse_n(n)

def reverse_n(n):
    return int(str(n)[::-1])

def palindrome_chain_length(n):
    chain_n = 0
    while is_palindrome(n) is False:
        n = n + reverse_n(n)
        chain_n += 1
    return(chain_n)
