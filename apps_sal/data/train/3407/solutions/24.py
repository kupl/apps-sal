def palindrome_chain_length(n):
    counter = 0
    x = str(n)[::-1]
    while str(n) != x:
        n = n + int(x)
        x = str(n)[::-1]
        counter += 1
    return counter
