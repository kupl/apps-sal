def is_palindrome(x):
    return str(x) == str(x)[::-1]

def palindrome_chain_length(n):
    counter = 0
    while not is_palindrome(n):
        n = n + int(str(n)[::-1])
        counter += 1
    return counter
