def palindrome_chain_length(n):
    a = 0
    x = str(n)
    while n != int(x[::-1]):
        x = str(n)
        n = n + int(x[::-1])
        x = str(n)
        a = a+1
    return a
