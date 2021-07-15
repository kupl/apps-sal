def palindrome_chain_length(n):
    x = 0
    while n != int(str(n)[::-1]):
        n = n + int(str(n)[::-1])
        x += 1
    return x

